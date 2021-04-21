from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Customer, Profile

from core.models import CustomerShippingAddress


class CustomerRegisterForm(UserCreationForm):
    class Meta:
        model = Customer
        fields = ['email', 'user_name', 'first_name', 'last_name', 'password1', 'password2']


class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs.update({
            'class': 'profile__input',
            'disabled': True
        })

        self.fields['last_name'].widget.attrs.update({
            'class': 'profile__input',
            'disabled': True
        })

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name']

class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class CustomerShippingAddressForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['full_name'].widget.attrs.update({
            'class': 'address__input',
            'placeholder': 'First and Last Name',
            'autocomplete': 'off'
        })

        self.fields['phone'].widget.attrs.update({
            'class': 'address__input',
            'placeholder': 'Please enter your phone number',
            'autocomplete': 'off'
        })

        self.fields['note'].widget.attrs.update({
            'class': 'address__input',
            'placeholder': 'Please enter your notes'
        })

        self.fields['house_no'].widget.attrs.update({
            'class': 'address__input',
            'placeholder': 'House No.',
            'autocomplete': 'off'
        })

        self.fields['zip_code'].widget.attrs.update({
            'class': 'address__input',
            'placeholder': 'Enter your zip code',
            'autocomplete': 'off'
        })

        self.fields['province'].widget.attrs.update({
            'class': 'address__input',
            'placeholder': 'Province of shipping/billing address',
            'autocomplete': 'off'
        })

        self.fields['city_municipality'].widget.attrs.update({
            'class': 'address__input',
            'placeholder': 'City/Municipality shipping/billing address',
            'autocomplete': 'off'
        })

        self.fields['barangay'].widget.attrs.update({
            'class': 'address__input',
            'placeholder': 'Barangay of shipping/billing address',
            'autocomplete': 'off'
        })



    class Meta:
        model = CustomerShippingAddress
        fields = ['full_name', 'phone', 'note', 'house_no', 'zip_code', 'province', 'city_municipality', 'barangay']
