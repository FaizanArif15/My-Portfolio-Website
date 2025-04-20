from django.shortcuts import render

# Create your views here.

from .models import Project, Certificate

def home(request):
    projects = Project.objects.all()
    certificates = Certificate.objects.all()
    return render(request, 'main/home.html', {
        'projects': projects,
        'certificates': certificates,
    })