from django.shortcuts import render
from django.http import HttpResponse

def addyourstartup(request):
    return HttpResponse("<h1>Hello World</h1>")