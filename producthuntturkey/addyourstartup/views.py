from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse

from .forms import AddYourStartupForm

def addyourstartup(request):
    form = AddYourStartupForm()

    if request.method == "POST":
        form = AddYourStartupForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your product was successfully submitted!")
            return redirect('add-your-startup')

    context = {
        'form': form
    }

    return render(request, 'add-your-startup.html', context)