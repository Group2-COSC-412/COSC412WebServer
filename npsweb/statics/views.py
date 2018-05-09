from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
import os

# Create your views here.
WK_DIR = os.path.dirname(os.path.abspath(__file__))


def css(request, file):
    pathlist = request.path.split('/')
    file = pathlist[len(pathlist) - 1]
    return HttpResponse(open(WK_DIR+'/css/'+file))


def fonts(request: HttpRequest):
    pathlist = request.path.split('/')
    file = pathlist[len(pathlist) - 1]
    return HttpResponse(open(WK_DIR+'/css/fonts/'+file))


def js(request: HttpRequest):
    pathlist = request.path.split('/')
    file = pathlist[len(pathlist) - 1]
    return HttpResponse(open(WK_DIR+'/js/'+file))
