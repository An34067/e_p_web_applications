from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def menu(request):
    return render(request, 'menu.html')

def reservation(request):
    return render(request, 'reservation.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def profile(request):
    return render(request, 'profile.html')