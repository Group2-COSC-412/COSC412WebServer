from django.shortcuts import render, redirect
from django.http import FileResponse
from django.template import loader
from django.views.decorators.csrf import csrf_protect
import os

# Create your views here.
WK_DIR = os.path.dirname(os.path.abspath(__file__))


# open(WK_DIR+'/html_files/'+file)
def index(request, file: str):
    if not file.endswith(".html"):
        file += ".html"
    return FileResponse(render(request, file))
