from django.contrib.auth.models import Group, User
from . import models
from django.db.models.signals import post_save


def consumerProfile(sender, instance,created,*args,**kwargs):
    if created:
        username = instance.username
        email = instance.email
        uid = instance.id
        group, created = Group.objects.get_or_create(name = 'consumer')
        instance.groups.add(group)
        models.consumers.objects.create(user = instance,username = username,email = email,id=uid)

post_save.connect(consumerProfile,sender=User)