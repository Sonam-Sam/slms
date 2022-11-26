from django.db import models
import uuid
from django.contrib.auth.models import User
from users.models import Profile
from django.utils import timezone
from datetime import datetime

class Leave(models.Model):
    student = models.ForeignKey(Profile, on_delete=models.CASCADE)
    LEAVE_TYPE = (
        ('Sick', 'Sick Leave'),
        ('Escote', 'Escote Leave'),
        ('Casual', 'Casual Leave'),
        ('Others', 'Others'),
    )
    leave = models.CharField(max_length=200, choices=LEAVE_TYPE)
    # sdate = models.DateTimeField(auto_now_add=False, auto_now=False, null=True, blank=True)
    # edate = models.DateTimeField(auto_now=True)
    
    startdate = models.DateField(verbose_name=('Start Date'),help_text='leave start date is on ..',null=True,blank=False)
    enddate = models.DateField(verbose_name=('End Date'),help_text='coming back on ...',null=True,blank=False)


    reason = models.TextField(blank=True, null=True)
    

    status = models.CharField(max_length=12, default='Pending', null=True) #pending,approved,rejected,cancelled
    is_approved = models.BooleanField(default=False) #hide

    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now_add=True)

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return str(self.student)
    
    class Meta:
        ordering = ['-created']

class Document(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created']

