from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Jam(models.Model):
    track_url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User)
