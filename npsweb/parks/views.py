from django.shortcuts import render
from django.http import FileResponse
import os

# Create your views here.
WK_DIR = os.path.dirname(os.path.abspath(__file__))


# open(WK_DIR+'/html_files/'+file)
def state(request, _state: str, file: str):
    if not file.endswith(".html"):
        file += ".html"
    return FileResponse(render(request, os.path.join(_state, file)))


def stateindex(_state: str):
    pass
