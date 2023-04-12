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

    if request.user.is_authenticated:
       profile=request.user.profile
    else:
        profile=None

    print(profile)

    form=ReviewForm()

    
    Number_of_reviewers=len(project.review_set.all())

    if request.method=="POST":
        form=ReviewForm(request.POST)
        if form.is_valid():
            review=form.save(commit=False)
            review.project=project
            review.owner=profile
            review.save()
            project.getVoteCount
            messages.success(request,'Your review is successfully saved!')
            return redirect('single_project',pk=project.title)



    context={'project':project,'tags':tags,'form':form,'profile':profile,'Number_of_reviewers':Number_of_reviewers}
    return render(request,'single_project.html',context)