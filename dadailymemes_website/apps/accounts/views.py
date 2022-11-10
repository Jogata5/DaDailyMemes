# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

def signin_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('public:index')
        else:
            messages.success(request, ("There was an error logging in"))
            return redirect('account:signin')

    else:
            return render(request,'signin.html', {}) ##auth login name unknown yet till CREATED

def signout_user(request):
    logout(request)
    messages.success(request, ("<PepeSadge emote>"))
    return redirect('public:index')

def signup_user(request): 
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate( username=username , password=password )
            login(request,user)
            messages.success(request,("Poggers, you're signed up"))
            return redirect('public:index')
    else:
        form = RegisterUserForm()

    return render(request,'signup.html',{
        'form':form,
        }) #instead of register its signup

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'profile.html'