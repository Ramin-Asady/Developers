from django.shortcuts import render,redirect

from django.contrib.auth import login,authenticate,logout

# Create your views here.

from django.contrib.auth.models import User

from . models import Profile
from projects.models import Project

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm

def loginPage(request):
    page='login'

    if request.method == 'POST' :
        username=request.POST['username']
        password=request.POST['password']

        try:
            User.objects.get(username=username)

        except:
              messages.error(request,'User does not exist')

        user=authenticate(request,username=username,password=password)

        if user is not None :
            login(request,user)
            cop='welcome  '+str(user.username)
            messages.success(request,cop)
            return redirect('projects')

        else:
            messages.error(request,'Username or password are incorrect')


    return render(request,'login_register.html',{'page':page})

def logoutUser(request):
    logout(request)
    messages.info(request,'User is successfully logged out')
    return redirect('login')

def registerUser(request):
    
    page='register'
    form=CustomUserCreationForm()
    context={'page':page,'form':form}


    if request.method == 'POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid() :
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            messages.success(request,'You are successfully registered')
            login(request,user)
            return redirect('projects')
        
        else:
            messages.error(request,'An error has occurred during registeration')
            return render(request,'login_register.html',{'form':form,'page':page})


    return render(request,'login_register.html',context)

def profiles(request):
    profiles=Profile.objects.all()
    
    return render(request,'profiles.html',{'profiles':profiles})

def user_profile(request,wk):

    data_profile=Profile.objects.get(username=wk)

    top_skill=data_profile.skill_set.exclude(description__exact="")
    other_skill=data_profile.skill_set.filter(description="")

    projects_data=Project.objects.filter(owner=data_profile)

    content={'data_profile':data_profile , 'projects_data':projects_data,'top_skill':top_skill,'other_skill':other_skill}

    return render(request,'user_profile.html',content)


@login_required(login_url='login')
def userAccount(request):
    profile=request.user.profile
    projects=profile.project_set.all()
    skills=profile.skill_set.all()

    context={'profile':profile,'projects':projects,'skills':skills}
    return render(request,'account.html',context)