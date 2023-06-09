from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.forms import ModelForm

from .models import Skill,Profile, Message

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','email','username','password1','password2']
        labels={'first_name':'Name'}


    def __init__(self,*args,**kwargs):
        super(CustomUserCreationForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
                field.widget.attrs.update({'class':'input' , 'placeholder':'Write here'})


class SkillForm(ModelForm):
    class Meta:
        model=Skill
        fields='__all__'
        exclude=['owner']


    def __init__(self,*args,**kwargs):
        super(SkillForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
                field.widget.attrs.update({'class':'input','placeholder':"Enter text"}) 

class ProfileForm(ModelForm):
    class Meta:
        model=Profile
        fields=['username','name','email','short_intro','bio','location',
               'profile_image','social_github','social_twitter',
                'social_linkedin','social_youtube','social_website']

        labels={'profile_image':'Avatar:'}

    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
                field.widget.attrs.update({'class':'input' , 'style':"font-size:20px;color:green;"})


class MessageForm(ModelForm):
    class Meta:
        model=Message
        fields=['name' , 'email' , 'subject' , 'body']

        labels={'name':'* Name:' , 'email': '* Email:' , 'subject':' Subject:' ,'body':'* Your Message:'}


    def __init__(self,*args,**kwargs):
        super(MessageForm,self).__init__(*args,**kwargs)

        for name,field in self.fields.items():
                if name=='email':
                   field.widget.attrs.update({'class':'input','placeholder':"example@email.com"})
                else:
                   field.widget.attrs.update({'class':'input','placeholder':"Enter text"}) 