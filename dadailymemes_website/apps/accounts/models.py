from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from datetime import datetime, timedelta
#from django import forms 

MEME_CATEGORIES = (
    ('animals','animals'),
    ('fail','fail'),
    ('confused','confused'),
    ('gaming','gaming'),

)

# Create your models here.

# class Genres(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     animals = models.BooleanField()
#     fail = models.BooleanField()
#     confused = models.BooleanField()
#     gaming = models.BooleanField()


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)   
    has_job = models.BooleanField(False)


    meme_categories = MultiSelectField(choices = MEME_CATEGORIES, null = True)

    def __str__(self):
        return self.user.username

# class EmailJob(models.Model):   
#     current_date = datetime.now()
#     delta = timedelta(days=1)
    
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     job_time = models.DateTimeField(auto_now=True)    
#     next_job = current_date + delta
#     gif = models.ImageField(null=False)
        
#     def __str__(self) -> str:
#         return self.user

    
"""

class UserPersona(models.Model):
    name = models.CharField(max_length=64, unique=True)
    normalized_name = models.CharField(max_length=64, unique=True)
    description = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

class CreateUserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")

    is_full_name_displayed = models.BooleanField(default=True)

    bio = models.CharField(max_length=500, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    persona = models.ForeignKey(UserPersona, on_delete=models.SET_NULL, blank=True, null=True)

"""

