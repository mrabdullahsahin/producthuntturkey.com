from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from .forms import AddYourStartupForm

def addyourstartup(request):
    form = AddYourStartupForm()
    
    context = {
        'form': form
    }

    if request.method == "POST":
        form = AddYourStartupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your product was successfully submitted!")
            return redirect('add-your-startup')
        else:
            return render(request, 'add-your-startup.html', context)
    else:
        return render(request, 'add-your-startup.html', context)

    return render(request, 'add-your-startup.html', context)