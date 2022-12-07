# from django.http import HttpResponse
# from django.template import loader
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages 
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm, UserProfileForm, UserUpdateForm, ProfileUpdateForm



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
        profile_form = UserProfileForm(request.POST)
        #form = RegisterForm(request.POST 
        if form.validUserName() or form.validEmail():
            username = form.fields.get('username')
            # squery = "SELECT * FROM auth_user WHERE username='"+username+"';"
            if form.is_valid() and profile_form.is_valid():
                user = form.save()

                proflie = profile_form.save(commit=False)
                proflie.user= user 

                proflie.save()

                username = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate( username=username , password=password )
                login(request,user)
                messages.success(request,("Poggers, you're signed up"))
                return redirect('public:index')
    else:
        form = RegisterUserForm()
        profile_form = UserProfileForm()
        #form = RegisterForm(request.POST)

    return render(request,'signup.html',{
        'form':form, 'profile_form' : profile_form
        }) #instead of register its signup

"""
def signup_user(request):
    form = RegisterUserForm(request.POST or None)
    if request.method == "POST":
        form.save()
        return redirect('public:index')
    context = {"form":form}
    return render(request, 'signup.html', context)
"""

def timer(request):
    return render(request, 'timer.html')


class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'profile.html'
    


 ##### work on update once home (UserProfile)####   
def profile_update(request):
    if request.method =='POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, instance= request.user)
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)


    return render(request, 'profile_update.html',{
        'user_form':user_form, 'profile_form':profile_form,
    })    

