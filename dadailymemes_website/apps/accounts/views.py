# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin

def signin(request):
    if request.method == 'POST':
        request.POST.get('username')
        request.POST.get('password')
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def quiz(request):
    return render(request, 'quiz.html')

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'profile.html'

##LoginRequiredMixin,TemplateView