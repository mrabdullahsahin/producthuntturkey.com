from django.shortcuts import render

def privacy_policy(request):
    return render(request, 'privacy-policy.html')

def terms_of_service(request):
    return render(request, 'terms-of-service.html')

def ambassadors(request):
    return render(request, 'ambassadors.html')

def what_is(request):
    return render(request, 'what-is-product-hunt.html')