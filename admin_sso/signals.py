from django.contrib.auth.models import User
from users.models import Profile
from .models import ssoProfile
from django.conf import settings

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

def updateAdmin(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

def editUser(sender, instance, created, **kwargs):
    profile = instance
    user = profile.user

    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()


def deleteUser(sender, instance, **kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass

post_save.connect(updateAdmin, sender=Profile)
post_save.connect(editUser, sender=ssoProfile)
post_delete.connect(deleteUser, sender=Profile) 