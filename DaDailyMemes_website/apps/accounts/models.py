from email.policy import default
from django.db import models

# Create your models here.

class CreateUserProfile(models.Model):
    is_full_name_displayed = models.BooleanField(default=True)