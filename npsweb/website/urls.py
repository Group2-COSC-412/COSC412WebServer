from django.urls import path

from . import views

urlpatterns = [
    path('', views.empty, name='redirect'),
    path('index', views.index, name='index')
]