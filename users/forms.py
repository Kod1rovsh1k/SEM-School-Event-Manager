from django import forms
from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class CustomLogin(AuthenticationForm):
    username = UsernameField(label='Enter Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CustomRegisterForm(UserCreationForm):
    username = UsernameField(label='Enter Username', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Enter Email', widget=forms.TextInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    groups = forms.ModelMultipleChoiceField(
        label='Groups',
        queryset=Group.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-select h-auto', 'style': 'min-height: 120px;'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['groups'].queryset = Group.objects.all()
        

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2", "groups")
