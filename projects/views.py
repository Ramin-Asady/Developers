from django.shortcuts import render , redirect
from .models import Project,Tag

from .forms import ReviewForm,ProjectForm

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.db.models import Q


def projects(request):
    search_query=''

    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')

    tags=Tag.objects.filter(name__icontains=search_query)

    projects=Project.objects.distinct().filter(Q(title__icontains=search_query) | Q(vote_total__icontains=search_query) |
                            Q(tags__in=tags) | Q(owner__username__icontains=search_query))

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


@login_required(login_url="login")
def createProject(request):
    profile=request.user.profile
    form=ProjectForm()

    if request.method== 'POST' :
        form=ProjectForm(request.POST,request.FILES)
        if form .is_valid():
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            messages.info(request,'Your project is successfully added!')
            return redirect("account")

    context={'form':form}
    return render(request,'project_form.html',context)

@login_required(login_url="login")
def updateProject(request,pk):
    profile=request.user.profile
    project=profile.project_set.get(id=pk)
    form=ProjectForm(instance=project)

    if request.method== 'POST' :
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form .is_valid():
            form.save()
            messages.success(request,'The selected project is successfully updated!')
            return redirect("account")

    return render(request,'project_form.html',{'form':form})


@login_required(login_url="login")
def deleteProject(request,pk):

    profile=request.user.profile
    project=profile.project_set.get(title=pk)
    project.delete()
    messages.info(request,'Project is successfully deleted!')

    return redirect('account')