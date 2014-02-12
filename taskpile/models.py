from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    teammates = models.ManyToManyField(User, related_name="teammates")

    def __unicode__(self):
        return u"%s" % (self.user)
    
class Task(models.Model):
    summary = models.CharField(max_length=200)
    details = models.TextField(blank=True)
    creator = models.ForeignKey(User, related_name="tasks_created")
    #assigned_users = models.ManyToManyField(User, related_name="tasks_assigned")

    assigned_user = models.ForeignKey(User, related_name="tasks_assigned")

    time_created = models.DateTimeField(auto_now_add=True)
    time_updated = models.DateTimeField(auto_now=True)
    completed = models.BooleanField( default=False )
    time_completed = models.DateTimeField(blank=True, null=True)
    
    def __unicode__(self):
        return u"%s" % (self.summary[:50])

    class Meta:
        ordering = ['-time_updated']


