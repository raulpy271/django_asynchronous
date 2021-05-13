from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Este app mostra de uma forma unificada informaçoes sobre linguagens de programaçao")


