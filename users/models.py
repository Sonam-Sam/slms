from random import choices
from django.db import models
from django.contrib.auth.models import User
import uuid

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    username = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    YEAR = (
        ('1', 'First'),
        ('2', 'Second'),
        ('3', 'Third'),
        ('4', 'Fourth'),
    )
    year = models.CharField(max_length=100, choices=YEAR)
    SEMESTER = (
        ('1', 'First'),
        ('2', 'Second'),
    )
    semester = models.CharField(max_length=200, choices=SEMESTER)
    COURSE = (
        ('Computer Science', 'Bsc CS'),
        ('Information Technology', 'Bsc IT'),
        ('School of Computing', 'SOC'),
        ('Fullstack', 'FS'),
    )
    course = models.CharField(max_length=200, choices=COURSE)
    GENDER = (
        ('Male', 'M'),
        ('Female', 'F'),
    )
    gender = models.CharField(max_length=100, choices=GENDER)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png")
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user)
