from django.shortcuts import render
from django.http import HttpResponse
from .models import  Store, StoreProfile, ProductCategory, Product
# Create your views here.


def index_page(request):
    return render(request, 'core/index.html')


def browsing_page(request):
    stores = Store.objects.all()
    products = ProductCategory.objects.all()
    context = {
        'stores': stores,
        'products': products
    }

    return render(request, 'core/browsing.html', context)

def store_page(request, store):
    return HttpResponse(f'Welcome to {store} shopping place')

def product_page(request, store, product):
    obj = Store.objects.get(slug=store)

    product = Product.objects.get(slug=product, store=obj)

    context = {
        "product": product,
    }
    return render(request, 'core/product.html', context)

def cart_page(request, user):
    return render(request, 'core/cart.html')

def profile_page(request, user):
    return render(request, 'core/profile.html')
