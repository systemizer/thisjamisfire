from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Jam(models.Model):
    track_url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile")
    following = models.ManyToManyField(User)


def create_profile(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        profile = UserProfile(user=user)
        profile.save()

post_save.connect(create_profile, sender=User)
