from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='login.html')),
    path('logout', views.usrLogout),
    path('create', views.createUser)
]
