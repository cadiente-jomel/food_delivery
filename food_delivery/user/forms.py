from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Profile


class CustomerRegisterForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['email', 'user_name', 'first_name', 'last_name', 'password1', 'password2']


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name']

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
