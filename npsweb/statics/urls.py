from django.urls import path

from . import views

urlpatterns = [
    path('indexstyle.css', views.indexstyle),
]
