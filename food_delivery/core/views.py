from django.shortcuts import render
from django.http import HttpResponse
from .models import  Store, StoreProfile
# Create your views here.


def index_page(request):
    return render(request, 'core/index.html')


def browsing_page(request):
    store = Store.objects.all()

    context = {
        'store': store
    }

    return render(request, 'core/browsing.html', context)

def cart_page(request, user):
    return render(request, 'core/cart.html')

def profile_page(request, user):
    return render(request, 'core/profile.html')
