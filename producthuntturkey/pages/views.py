from django.shortcuts import render

def privacy_policy(request):
    return render(request, 'privacy-policy.html')