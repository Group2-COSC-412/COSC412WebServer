from django.shortcuts import render
from django.http import HttpResponse
from elasticsearch import Elasticsearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth
from django.http import HttpRequest

# Create your views here.


def login(request: HttpRequest):
    # if username and password in db, login, otherwise return error
    pass
