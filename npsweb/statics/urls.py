from django.urls import path

from . import views

urlpatterns = [
    path('css/', views.css),
    path('fonts/', views.fonts),
    path('js/', views.js)
]
