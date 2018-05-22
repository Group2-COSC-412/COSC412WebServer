from django.shortcuts import render
from django.http import FileResponse, HttpResponse
import os

# Create your views here.
WK_DIR = os.path.dirname(os.path.abspath(__file__))


def statics(request, file: str):
    if file.endswith('.css'):
        return HttpResponse(open(WK_DIR+'/static_files/'+file), content_type='text/css')
    elif file.endswith('.js'):
        return HttpResponse(open(WK_DIR+'/static_files/'+file), content_type='application/javascript')
    elif file.endswith('.zip'):
        response = HttpResponse(open(WK_DIR+'/static_files/'+file, 'rb').read(), content_type='application/zip')
        response['Content-Disposition'] = 'attachment;filename=' + file
        return response
    return FileResponse(open(WK_DIR+'/static_files/'+file, 'rb'))
