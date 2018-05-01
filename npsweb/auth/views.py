from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.


def usrLogin(request: HttpRequest):
    if request.method == 'GET':
        return redirect('https://national-parks.fcgit.net/login')
    else:
        # if username and password in db, login, otherwise return error
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('https://national-parks.fcgit.net/')
        else:
            # TODO Return error message
            pass


def createUser(request: HttpRequest):
    # TODO email validation
    pass
