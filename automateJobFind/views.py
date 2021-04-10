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
        output_filename = (request.session['_old_post'])["name"]+"_.pdf"
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
    return render(request, 'automateJobFind\\resume.html', context)


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
            send_mail(f"{old_post['name']} <{old_post['email']}>", old_post["email"], "Job Application",
                      "Dear Sir/Madam,\nI am " +
                      old_post["name"]+" who are majoring in " +
                      old_post["category"]
                      + ". I would like to apply for the " +
                      eachList["position"] +
                      " in  your company (" + eachList["company"] + "). "
                      + "Attached is my resume for your perusal. I look forward to hearing back from you. Please feel free to contact me with any questions. You can reach me by phone: "
                      + old_post["contact"] + " or " + old_post["email"] +
                      ".\n\nThank you for your consideration.\n\nSincerely,\n"
                      + old_post["name"], [DIRNAME+"/../"+old_post["name"]+"_.pdf"])
        return redirect('/')
    return render(request, 'automateJobFind/joblist.html', context)
