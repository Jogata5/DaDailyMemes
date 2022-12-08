from django.contrib import admin
from .models import UserProfile, EmailJob, Genres

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(EmailJob)
admin.site.register(Genres)