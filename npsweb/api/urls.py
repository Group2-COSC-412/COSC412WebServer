from django.urls import path

from . import views

urlpatterns = [
    path('es-GET', views.esGET),
    path('es-POST', views.esPOST)
]