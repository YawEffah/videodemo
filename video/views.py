from django.shortcuts import render
from .forms import *
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))


    return render(request, 'video/index.html', {})

def signup_view(request): 
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))  
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            logout(request)
            return HttpResponseRedirect(reverse('login'))
        else:
            return render(request, 'video/signup.html', {'signup':form})   
    return render(request, 'video/signup.html', {'signup':UserCreationForm()})

def login_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']        
        user = authenticate(request, username=username, password = password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
        else:
            return render(request, 'video/login.html', {'login': LoginForm(request.POST), 'message':"Invalid Credentials"})

    return render(request, 'video/login.html', {'login': LoginForm()})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


