from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.utils.text import slugify
import json

from .models import  Store, StoreProfile, ProductCategory, Product, Cart
# Create your views here.

# page views !
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

def product_page(request, store, product):
    obj = Store.objects.get(slug=store)

    product = Product.objects.get(slug=product, store=obj)

    obj = ProductCategory.objects.get(product=product)

    context = {
        "obj": obj,
    }
    return render(request, 'core/product.html', context)

def cart_page(request, user):
    return render(request, 'core/cart.html')

def profile_page(request, user):
    return render(request, 'core/profile.html')

def store_page(request, store):
    # most sell product
    obj = Store.objects.get(slug=store)

    store = StoreProfile.objects.get(store=obj)
    products = ProductCategory.objects.filter(product__store=store.store)
    context = {
        'store': store,
        'products': products,
    }

    return render(request, 'core/store.html', context)

# page views!

# ajax part!
def cart_add(request):

    payload = json.loads(request.body.decode('utf-8'))
    
    product_slug = slugify(payload.get('productName'))
    if request.user.is_authenticated:
        try:
            store_name = Store.objects.get(slug=payload.get('productSold'))
            product = Product.objects.get(slug=product_slug, store=store_name)
            cart = Cart.objects.create(product=product, customer=request.user)

            print(cart)
            print(store_name)
        except Exception as e:
            print(e)

        return JsonResponse({'message': 'Product added to your cart'})

    return JsonResponse({'message': 'Not Logged in'})

