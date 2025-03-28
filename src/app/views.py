from django.shortcuts import render


def view(request):
    return render(
        request,
        'home/index.html'
    )

def profile(request):
    return render(
        request,
        'profile/profile.html'
    )