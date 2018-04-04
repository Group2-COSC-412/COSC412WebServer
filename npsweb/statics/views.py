from django.shortcuts import render
from django.http import HttpResponse
import os

# Create your views here.
WK_DIR = os.path.dirname(os.path.abspath(__file__))

def indexstyle(request):
    return HttpResponse(open(WK_DIR+'/css/indexstyle.css'))
