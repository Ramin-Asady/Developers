from django.shortcuts import render,redirect

from django.contrib.auth import login,authenticate,logout

# Create your views here.

from django.contrib.auth.models import User

from django.contrib import messages

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

def logoutUser(request):
    logout(request)
    messages.info(request,'User is successfully logged out')
    return redirect('login')