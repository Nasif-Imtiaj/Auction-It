from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from register.forms import forms
# Create your views here.



class RegisterCreateView(CreateView):
    form_class = UserCreationForm()
    template_name = 'register/register.html'
    success_url = '/'

def register(response):
    form = UserCreationForm()
    return render(response, "register/register.html",{"form":form})