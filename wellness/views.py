from django.shortcuts import render

def index(request):
    return render(request, 'wellness/index.html')

def about(request):
    return render(request, 'wellness/about.html')

def contact(request):
    return render(request, 'wellness/contact.html')

def services(request):
    return render(request, 'wellness/services.html')