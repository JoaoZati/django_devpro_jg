from django.http import HttpResponse # noqa
from django.shortcuts import render

from modulos import facade


def home(request):
    return render(request, 'base/home.html', {'MODULOS': facade.listar_modulos_ordenados()})
