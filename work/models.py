''' Todos models declared here '''
from __future__ import unicode_literals
from django.db import models

from django.contrib.auth.models import User

from django.utils import timezone

class todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(blank=True, null=True)
    is_finished = models.BooleanField(default=False)
    priority = models.CharField(max_length=1)
    def __unicode__(self):
        return self.user.username+" "+self.title

class tags(models.Model):
    todo = models.ForeignKey(todo, on_delete=models.CASCADE)
    tagname = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True, null=True);
