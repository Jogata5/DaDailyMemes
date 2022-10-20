
from django.urls import path

# from DaDailyMemes.DaDailyMemes_website.views import index
from . import views

app_name="public"
urlpatterns = [
    path("profile", views.ProfileView, name="profile"),
    path('', views.index, name="index"),
    path('about', views.about, name="about"),
    path('contact', views.contact, name="contact"),

    
]