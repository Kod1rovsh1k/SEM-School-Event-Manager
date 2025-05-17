from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import View

from .forms import CustomLogin, CustomRegisterForm
from django.contrib.auth.models import Group
from django.contrib.auth.models import User


# Create your views here.
class UserLoginView(View):
    def get(self, request):
        form = CustomLogin()
        return render(request, 'users/user_login.html', {'form': form})

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        tmp = request.GET.get("next")
        back_url = tmp if tmp is not None else 'index'
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"You logged in as: {username}")
            return redirect(back_url)
        else:
            messages.error(request, "Invalid username or password")
            return redirect("login")


class UserRegisterView(View):
    def get(self, request):
        form = CustomRegisterForm()
        return render(request, "users/user_register.html", {"form": form})

    def post(self, request):
        tmp = request.GET.get("next")
        back_url = tmp if tmp is not None else 'index'
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            # Перевірка, чи серед обраних груп є "Викладач"
            selected_groups = form.cleaned_data['groups']
            if any(group.name == 'Викладач' for group in selected_groups):
                user.is_staff = True
            user.save()
            for group in selected_groups:
                user.groups.add(group)
            login(request, user)
            return redirect(back_url)
        return render(request, "users/user_register.html", {"form": form})


class UserLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("index")


class UserProfileView(LoginRequiredMixin, View):
    login_url = reverse_lazy('login')
    def get(self, request):
        return render(request, 'users/user_profile.html', {'user': request.user})