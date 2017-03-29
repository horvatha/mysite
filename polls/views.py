from django.shortcuts import render
from django.http import HttpResponse


def rendszam(request):
    return HttpResponse("<h1>Hurrá</h1>")


def index(request):
    return render(request, 'polls/index.html')
