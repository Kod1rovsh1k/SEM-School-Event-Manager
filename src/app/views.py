from django.shortcuts import render


def view(request):
    return render(request, 'home/home.html')


def register(request):
    return render(request, 'register/register.html')
