# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')
class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/profile.html'