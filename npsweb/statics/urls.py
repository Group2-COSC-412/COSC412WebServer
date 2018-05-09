from django.urls import path

from . import views

urlpatterns = [
    path(r'css/(.*?)', views.css),
    path(r'fonts/(.*?)', views.fonts),
    path(r'js/(.*?)', views.js)
]
