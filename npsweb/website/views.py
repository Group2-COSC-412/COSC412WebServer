from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import os

# Create your views here.
WK_DIR = os.path.dirname(os.path.abspath(__file__))

def index(request):
    template = loader.get_template('website/index.html')
    return HttpResponse(template.render(request=request))
