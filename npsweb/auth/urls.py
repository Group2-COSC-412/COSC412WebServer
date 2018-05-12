from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('login', redirect('/home/login')),
    path('logout', views.usrLogout),
    path('create', views.createUser)
]
