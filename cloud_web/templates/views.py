# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserLoginForm, UserRegistrationForm
from cloud_web.models import Kisi
from django.http import HttpResponse
import requests

def redirect_to_login(request):
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return render(request, 'login_success.html',{'email':email})
            else:
                return redirect('register')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            kisi = Kisi(KisiMail=email,KisiPassword=password)
            kisi.save()
            login(request, kisi)
            return render(request, 'register_success.html',{'email':email})
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def index(request):
    response = requests.get('http://164.92.98.40')
    
    data = response.json()
    return render(request,'list.html',{'data':data})