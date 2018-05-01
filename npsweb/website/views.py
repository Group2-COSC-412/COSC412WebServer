from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect
import os

# Create your views here.


def empty(request):
    return redirect('https://national-parks.fcgit.net/home/index')


def index(request):
    template = loader.get_template('website/index.html')
    return HttpResponse(template.render(request=request))
