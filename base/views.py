from django.http import HttpResponse # noqa
from django.shortcuts import render # noqa

from modulos import facade


def home(request):
    return render(request, 'base/home.html', {})
