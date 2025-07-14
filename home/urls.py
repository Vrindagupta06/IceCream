from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignupPage, name='signup'),
    path('home/', views.HomePage, name='home'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutPage, name='logout'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('choose_flavour/', views.choose_flavour, name='choose_flavour'),
    path('show_flavour/', views.show_flavour, name='show_flavour'),
    ]
