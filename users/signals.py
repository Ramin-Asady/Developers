from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User

from .models import Profile

from django.core.mail import send_mail
from django.conf import settings


def createUpdated(sender,instance,created,**kwargs):
    if created :
        user=instance
        if user.username :
            profile=Profile.objects.create(
            user=user,
            username=user.username,
            name=user.first_name,
            email=user.email,
        )

        subject= 'Welcome to Developers  ' + str(user.first_name)
        mess1= 'Dear ' + str(user.first_name) +' Welcome to Developers\n' + 'Here is your login information\n'
        mess2= 'Username: ' + str(user.username) +'\n' +'You can modify your profile here:\n'+'http://127.0.0.1:8000/edit_account'
        message= mess1 + mess2 

        send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [profile.email],
                fail_silently=False,
            )


def profileUpdate(sender,instance,created,**kwargs):
    profile=instance
    user=profile.user
    
    if created == False:
        user.first_name=profile.name
        user.email=profile.email
        user.username=profile.username
        user.save()

post_save.connect(createUpdated,sender=User)

post_save.connect(profileUpdate,sender=Profile)


@receiver(post_delete,sender=Profile)
def deleteProfile(sender,instance,**kwargs):
    try:
        user=instance.user
        user.delete()
    except:
        pass

