from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

# Create your views here.


def usrLogin(request: HttpRequest):
    if request.method == 'GET':
        # TODO redirect to login page
        pass
    else:
        # if username and password in db, login, otherwise return error
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            # TODO redirect to home or profile or something
        else:
            # TODO Return error message
            pass


def createUser(request: HttpRequest):
    # TODO email validation
    pass
