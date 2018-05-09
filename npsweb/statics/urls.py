from django.urls import path

from . import views

urlpatterns = [
    path('statics/<path:file>', views.statics),
]
