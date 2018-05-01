from django.urls import path

from . import views

urlpatterns = [
    path('login', views.usrLogin),
    path('create', views.createUser)
]
