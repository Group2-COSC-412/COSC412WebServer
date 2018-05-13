from django.http import HttpRequest, HttpResponse
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from ..npsweb import settings

# Create your views here.
@csrf_protect
def createUser(request: HttpRequest):
    try:
        """
        username: 150 chars or fewer
        email: valid email address
        password: arbitrary length, any character
        fname: 30 chars or fewer
        lname: 150 chars of fewer
        
        :return: either success message or failure message (with reason) if POST, otherwise
            redirect to user creation page
        """
        if request.method == "POST" and\
                "email" in request.POST and\
                "psw-repeat" in request.POST and \
                "psw" in request.POST and\
                "first" in request.POST and\
                "last" in request.POST:
            user = User.objects.create_user(username=request.POST.get("email"),
                                            email=request.POST.get("email"),
                                            password=request.POST.get("password"))
            user.first_name = request.POST.get("first")
            user.last_name = request.POST.get("last")

            user.save()
            return redirect('https://national-parks.fcgit.net/home/login')
        elif request.method == "GET":
            return redirect('https://national-parks.fcgit.net/home/login')
    except Exception as e:
        log = open(settings.BASE_DIR + 'usercreatelog.txt')
        log.write(str(e))
        return HttpResponse("something went wrong")
