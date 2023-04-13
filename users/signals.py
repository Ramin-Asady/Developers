from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User

from .models import Profile


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
