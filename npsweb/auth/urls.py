from django.urls import path

from . import views

urlpatterns = [
    path('login', views.usrLogin),
    path('logout', views.usrLogout),
    path('create', views.createUser)
]
