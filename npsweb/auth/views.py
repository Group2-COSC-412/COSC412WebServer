from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect

# Create your views here.


def usrLogin(request: HttpRequest):
    if request.method == 'GET':
        return redirect('https://national-parks.fcgit.net/home/login')
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


def usrLogout(request: HttpRequest):
    logout(request)
    redirect('https://national-parks.fcgit.net/')


def createUser(request: HttpRequest):
    """
    username: 150 chars or fewer
    email: valid email address
    password: arbitrary length, any character
    fname: 30 chars or fewer
    lname: 150 chars of fewer

    :return: either success message or failure message (with reason) if POST, otherwise
        redirect to user creation page
    """
    if request.method == "POST" and\
            "username" in request.POST and\
            "email" in request.POST and \
            "password" in request.POST and\
            "fname" in request.POST and\
            "lname" in request.POST:
        user = User.objects.create_user(request.POST.get("username"),
                                        request.POST.get("email"),
                                        request.POST.get("password"))
        user.first_name = request.POST.get("fname")
        user.last_name = request.POST.get("lname")

        user.save()

    elif request.method == "GET":
        # TODO
        return redirect('https://national-parks.fcgit.net/home/login')
    pass
