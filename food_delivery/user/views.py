from django.core import serializers
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse

import json

from .forms import CustomerRegisterForm, CustomerForm, CustomerProfileForm, CustomerShippingAddressForm

from .models import Customer
from core.models import CustomerShippingAddress
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
    customer_address_form = CustomerShippingAddressForm()

    address_book = CustomerShippingAddress.objects.filter(customer=request.user)
    context = {
        'customer_form': customer_form,
        'address_form': customer_address_form,
        'address_book': address_book,
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

def add_address(request):
    payload = request.body.decode('utf-8')
    data = json.loads(payload)
    form = CustomerShippingAddressForm(data)
    form.data['customer'] = request.user


    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'Address Added', 'data': payload})
    return JsonResponse({'message': 'Error occured'})

def fetch_address(request, pk):
    address = CustomerShippingAddress.objects.get(pk=pk)
    serialize = serializers.serialize('json', [address, ], fields=('full_name', 'phone', 'house_no', 'zip_code', 'province', 'city_municipality', 'barangay', 'note'))

    obj = json.loads(serialize)

    data = json.dumps(obj[0])

    return JsonResponse(data, safe=False)

def edit_address(request, pk):
    payload = json.loads(request.body.decode('utf-8'))
    address = CustomerShippingAddress.objects.get(pk=pk)
    form = CustomerShippingAddressForm(instance=address)

    if form.is_valid():
        form.save()
        return JsonResponse({'message': 'address updated'})

    return JsonReponse({'message': 'error occured'})
# Ajax
