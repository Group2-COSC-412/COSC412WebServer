from django.urls import path
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('login', views.logins),
    path('logout', views.usrLogout),
    path('create', views.createUser)
]
