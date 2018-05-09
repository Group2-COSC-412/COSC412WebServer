from django.urls import path

from . import views

urlpatterns = [
    path('<path:file>', views.index, name='index')
]