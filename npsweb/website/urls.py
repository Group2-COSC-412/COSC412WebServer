from django.urls import path

from . import views

urlpatterns = [
    path('', views.empty, name='redirect'),
    path('<path:file>', views.index, name='index')
]