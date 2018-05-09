from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import os

# Create your views here.
WK_DIR = os.path.dirname(os.path.abspath(__file__))


def statics(request, file):
    pathlist = request.path.split('/')
    return HttpResponse(open(WK_DIR+'/statics/'+file))
