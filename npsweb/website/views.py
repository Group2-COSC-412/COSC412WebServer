from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
import os

# Create your views here.
WK_DIR = os.path.dirname(os.path.abspath(__file__))

def empty(request):
    return redirect('https://national-parks.fcgit.net/home/index')


def index(request, file: str):
    if not file.endswith(".html"):
        file += ".html"
    return HttpResponse(open(WK_DIR+'/html_files/'+file))
