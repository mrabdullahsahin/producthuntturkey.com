from django.shortcuts import render

def addyourstartup(request):
    return render(request, 'add-your-startup.html')