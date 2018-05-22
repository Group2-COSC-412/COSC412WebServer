from django.shortcuts import render
from django.http import FileResponse
from django.contrib.auth.decorators import login_required

import os

# Create your views here.
WK_DIR = os.path.dirname(os.path.abspath(__file__))


@login_required(login_url="/home/login")
def state(request, _state: str, file: str):
    if not file.endswith(".html"):
        file += ".html"
    return FileResponse(render(request, os.path.join(_state, file)))


@login_required(login_url="/home/login")
def stateindex(request, _state: str):
    return FileResponse(render(request, os.path.join(_state, 'index.html')))
