from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import os

# Create your views here.
WK_DIR = os.path.dirname(os.path.abspath(__file__))


def statics(request, file):
    return HttpResponse(open(WK_DIR+'/static_files/'+file))
