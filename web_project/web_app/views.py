from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.

def home(request):
    featured_dishes = Menu.objects.filter(is_available=True).order_by('?')[:3]
    return render(request, 'home.html', {'featured_dishes': featured_dishes})

def menu(request):
    search = request.GET.get('q', '') 
    category = request.GET.get('category', '')
    dishes = Menu.objects.filter(is_available=True)
    
    if search:
        dishes = dishes.filter(dish_name__icontains=search)

    if category:
        dishes = dishes.filter(dish_name__icontains=search)
    
    return render(request, 'menu.html', {
        'dishes': dishes,
        'category': category,
        'search': search 
    })

def dish_details(request, dish_id):
    dish = get_object_or_404(Menu, id=dish_id, is_available=True)
    return render(request, 'dish_details.html', {'dish': dish})

def reservation(request):
    available_tables = Tables.objects.filter(status='free')
    return render(request, 'reservation.html', {'available_tables': available_tables})


def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')

def profile(request):
    customer = Customers.objects.first()
    return render(request, 'profile.html', {'customer': customer})