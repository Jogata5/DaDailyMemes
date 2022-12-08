from django.contrib import admin
from .models import UserProfile, Genres, EmailJobs

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Genres)
admin.site.register(EmailJobs)