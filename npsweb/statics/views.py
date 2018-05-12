from django.shortcuts import render
from django.http import FileResponse
import os

# Create your views here.
WK_DIR = os.path.dirname(os.path.abspath(__file__))


def statics(request, file):
    return FileResponse(open(WK_DIR+'/static_files/'+file))
