import os
from django.shortcuts import render, redirect
from .forms import ResumeForm
from .rpaScrapper.index import get_job_list
from django.http import HttpResponse
from django.views.generic import View
from django.template.loader import get_template
from .utils import render_to_pdf
from xhtml2pdf import pisa
from .rpaMail.index import send_mail  # import python module


# Create your views here.
DIRNAME = os.path.dirname(__file__)
JOBPAGE_FOLDER = DIRNAME + "\\templates\\automateJobFind\\resume.html"


def home(request):
    form = ResumeForm()
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        request.session['_old_post'] = request.POST
        if form.is_valid():
            form.save()
            return redirect('/pdf')
    context = {'form': form}
    return render(request, 'automateJobFind/questionPage.html', context)


class GeneratePdf(View):

    def get(self, request, *args, **kwargs):
        output_filename = "test1.pdf"
        data = {'post': request.session['_old_post']}
        template = get_template(JOBPAGE_FOLDER)
        html = template.render(data)
        result_file = open(output_filename, "w+b")

        pisa_status = pisa.CreatePDF(
            html,
            dest=result_file)

        result_file.close()

        return redirect('/list')


def resume(request):
    old_post = request.session.get('_old_post')
    context = {'post': old_post}
    return render(request, 'automateJobFind\resume.html', context)


def list(request):
    scrapList = get_job_list
    old_post = request.session.get('_old_post')
    firstFilter = []
    secondFilter = []

    address = ((old_post["address"]).replace(',', '')).split()
    category = old_post["category"]

    # filter location
    for eachList in scrapList():
        for eachString in address:
            if eachString in eachList["location"]:
                if(eachList not in firstFilter):
                    firstFilter.append(eachList)

    # filter job category
    for eachList in firstFilter:
        if (eachList["category"] == category):
            secondFilter.append(eachList)

    context = {'joblist': secondFilter, 'post': old_post}
    if request.method == 'POST':
        for eachList in secondFilter:
            send_mail(old_post["name"], eachList["email"], "Job Application",
                      "Hello world", [DIRNAME+"/../test1.pdf"])
    return render(request, 'automateJobFind/joblist.html', context)

# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         data = {'post': request.session['_old_post']}
#         template = get_template(JOBPAGE_FOLDER)
#         html = template.render(data)
#         pdf = render_to_pdf(JOBPAGE_FOLDER, data)
#         if pdf:
#             response = HttpResponse(pdf, content_type='application/pdf')
#             filename = "Resume_%s.pdf" % ("12341231")
#             content = "inline; filename='%s'" % (filename)
#             download = request.GET.get("download")
#             content = "attachment; filename=%s" % (filename)
#             response['Content-Disposition'] = content
#             return response
#         return HttpResponse("Not found")
