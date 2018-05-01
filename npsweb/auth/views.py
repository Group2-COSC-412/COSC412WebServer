from django.shortcuts import render
from django.http import HttpResponse, H
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from django.http import HttpRequest
from django.contrib.auth import authenticate, login

# Create your views here.


def login(request: HttpRequest):
    # if username and password in db, login, otherwise return error
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if not user:
        login(request, user)
    else:
        # Return error message
        pass
