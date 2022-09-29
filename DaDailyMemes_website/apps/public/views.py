# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'index.html')
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render({}, request))

def about(request):
    return render(request, 'about.html')

# def signin(request):
#     return render(request, 'signin.html')

def contact(request):
    return render(request, 'contact.html')

# def signup(request):
#     return render(request, 'accounts/signup.html')

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'accounts/profile.html'
