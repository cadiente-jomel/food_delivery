from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import CustomerRegisterForm
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
