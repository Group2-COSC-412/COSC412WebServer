from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login', auth_views.LoginView.as_view(template_name='login.html', next='https://national-parks.fcgit.net/home/states')),
    path('logout', auth_views.LogoutView.as_view(next_page='https://national-parks.fcgit.net/home/index')),
    path('create', views.createUser)
]
