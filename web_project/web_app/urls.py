from django.urls import path, include
from web_app import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.menu, name='menu'),
    path('dish/<int:dish_id>/', views.dish_details, name='dish_details'),
    path('reservation/', views.reservation, name='reservation'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile')
]