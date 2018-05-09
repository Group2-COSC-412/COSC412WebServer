from django.urls import path

from . import views

urlpatterns = [
    path('css/<path:file>', views.css),
    path('fonts/<path:file>', views.fonts),
    path('js/<path:file>', views.js)
]
