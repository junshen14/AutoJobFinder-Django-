from django.shortcuts import render, redirect
from .forms import ResumeForm

# Create your views here.


def home(request):
    form = ResumeForm()
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'automateJobFind/questionPage.html', context)
