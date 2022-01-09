from django.shortcuts import render

def openpage(request):
    return render(request, 'open-startup.html')