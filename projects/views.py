from django.shortcuts import render
from .models import Project

# Create your views here.
def index(request):
    context = {'projects': Project.objects.all()}
    return render(request, 'projects/index.html', context)

def detail(request, project_id):
    project = Project.objects.get(id=project_id)
    context = {'project': project}
    return render(request, 'projects/detail.html', context)