from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    # fetured_dishes = Menu.objects.filter(is_available=True).order_by('?')[:3]
    # context = {
    #     'fetured_dishes': fetured_dishes,
    # }
    # return render(request, 'home.html', context)
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