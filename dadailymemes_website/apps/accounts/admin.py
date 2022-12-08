from django.contrib import admin
from .models import UserProfile, Genre

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Genre)