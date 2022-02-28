from ast import Name
from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginUser),
    path('registerUser', views.registerUser),
    path('register', views.register),
    path('login', views.login),
    path('login_success', views.login_success),
    path('log_out', views.log_out),
]