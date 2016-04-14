from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Authorization models

def upload_profile(instance, filename):
    return 'profile/%s.jpg'%instance.user.username

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    phone = models.CharField(max_length=11, blank=True)
    birthdate = models.DateField(null=True)
    gender = models.CharField(max_length=1)
    picture = models.ImageField(upload_to=upload_profile, blank=True)
    ipAddress = models.CharField(max_length=20, blank=True)
    def __unicode__(self):
        return self.user.first_name
