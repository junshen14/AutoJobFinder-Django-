from django.shortcuts import render, redirect
from .forms import ResumeForm
from .rpaScrapper.index import get_job_list

# Create your views here.


def home(request):
    form = ResumeForm()
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        request.session['_old_post'] = request.POST
        if form.is_valid():
            form.save()
            return redirect('/list')
    context = {'form': form}
    return render(request, 'automateJobFind/questionPage.html', context)


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
    return render(request, 'automateJobFind/joblist.html', context)
