from django.urls import path

from . import views

urlpatterns = [
    path('es', views.es),
]