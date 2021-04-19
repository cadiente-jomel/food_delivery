from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

import json

from .forms import CustomerRegisterForm, CustomerForm, CustomerProfileForm
# Create your views here.

def register_page(request):
    form = CustomerRegisterForm()
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('login-page')

    context = {
        'form': form
    }

    return render(request, 'user/register.html', context)

def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        customer = authenticate(request, email=email, password=password)

        if customer is not None:
            login(request, customer)

        return redirect('index-page')

    return render(request,'user/login.html')


def logout_page(request):
    logout(request)

def profile_page(request):
    customer_form = CustomerForm(instance=request.user)
    context = {
        'customer_form': customer_form,
    }
    return render(request, 'user/profile.html', context)

def profile_photo(request):
    pass


# Ajax
def profile_upload(request):
    if request.method == 'POST':
        payload = json.loads(request.body.decode('utf-8'))
        customer_data = {
            'first_name': payload.get('firstName'),
            'last_name': payload.get('lastName')
        }

        customer_form = CustomerForm(customer_data, instance=request.user)
        if customer_form.is_valid():
            customer_form.save()
            return JsonResponse({'message': 'Profile Updated'})
    return JsonResponse({'message': 'error'})
# Ajax
