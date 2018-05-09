from django.shortcuts import redirect


def empty(request):
    return redirect('https://national-parks.fcgit.net/home/index')