from django.http import HttpResponse # noqa
from django.shortcuts import render # noqa


def home(request):
    return render(request, 'base/home.html', {})
