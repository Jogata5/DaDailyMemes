# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.views.generic.base import TemplateView 
from django.contrib.auth.mixins import LoginRequiredMixin
from .giphy import get_gif


def index(request):
    gif = get_gif()
    context = {'gif_img' : gif}
    return render(request, 'index.html',context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def timer(request):
    return render(request, 'timer.html')

class ProfileView(LoginRequiredMixin,TemplateView):
    template_name = 'account/profile.html'

def giphy_test(request):
    gif = get_gif()
    context = {'gif_img' : gif}
    return render(request, 'giphy_test.html', context)

#class ProfileView(LoginRequiredMixin,TemplateView):
#    template_name = 'account/profile.html'
