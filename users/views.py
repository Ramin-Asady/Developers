from django.shortcuts import render,redirect

from django.http import HttpResponse

from django.contrib.auth import login,authenticate,logout

# Create your views here.

from django.contrib.auth.models import User

from . models import Profile, Skill
from projects.models import Project

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import CustomUserCreationForm , SkillForm , ProfileForm

from django.db.models import Q

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
    profile=Profile.objects.exclude(Q(bio = "") | Q(short_intro = None))
    search_query=''

    if request.GET.get('search_query'):
        search_query=request.GET.get('search_query')

    skills=Skill.objects.filter(name__iexact=search_query)

    profiles=profile.distinct().filter(Q(name__icontains=search_query) | Q(bio__icontains=search_query) | 
                                  Q(short_intro__icontains=search_query) | Q(skill__in=skills) )

    
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


@login_required(login_url='login')
def createSkill(request):
    profile=request.user.profile
    form=SkillForm()
    context={'form':form}

    if request.method == "POST":
        form=SkillForm(request.POST)

        if form.is_valid():
            skill=form.save(commit=False)
            skill.owner=profile
            skill.save()
            messages.success(request,'Your new skill has successfully added! ')
            return redirect('account')

    return render(request,'skill_form.html',context)


@login_required(login_url='login')
def editSkill(request,pk):
    profile=request.user.profile
    skill=profile.skill_set.get(id=pk)
    form=SkillForm(instance=skill)
    context={'form':form}

    if request.method=="POST":
        form=SkillForm(request.POST,instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request,'The selected skill has successfully been updated! ')
            return redirect('account')

    return render(request,'skill_form.html',context)


@login_required(login_url='login')
def deleteSkill(request,pk):
    profile=request.user.profile
    skill=profile.skill_set.get(id=pk)
    skill.delete()

    messages.success(request,'The selected skill has successfully been deleted! ')
    return redirect('account')

@login_required(login_url='login')
def editAccount(request):
    profile=request.user.profile
    form=ProfileForm(instance=profile)

    if request.method == "POST":
        form=ProfileForm(request.POST, request.FILES ,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'You are successfully edited your profile!')
            return redirect('account')

    context={'form':form}
    return render(request,'edit_account.html',context)


@login_required(login_url='login')
def deleteAccount(request,wk):
       
       profile1=request.user.profile
       profile2=Profile.objects.get(id=wk)
       if profile1==profile2 :
            user=profile1.user
            if request.method == "POST":
          
                user.delete()
                messages.info(request,"Now you are not a subscriber!")
                return redirect('projects')

            return render(request,'delete_account.html')

       else:
            return HttpResponse("An error occurred")