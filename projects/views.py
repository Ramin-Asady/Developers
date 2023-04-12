from django.shortcuts import render , redirect
from .models import Project

from .forms import ReviewForm

from django.contrib import messages

# Create your views here.

def projects(request):
    projects=Project.objects.all()

    return render(request,'projects.html' , {"projects":projects})

def single_project(request,pk):
    project=Project.objects.get(title=pk)
    tags=project.tags.all()

    context={'project':project,'tags':tags}
    return render(request,'single_project.html',context)