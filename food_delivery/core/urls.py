from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_page, name='index-page'),
    path('browsing/', views.browsing_page, name='browsing-page'),
    path('products/<str:store>/<str:product>', views.product_page, name='product-page'),
    path('stores/<str:store>/', views.store_page, name='store-page'),
    path('cart/<str:user>/', views.cart_page, name='cart-page'),
    path('profile/<str:user>/', views.profile_page, name='profile-page'),

    # ajax links
    path('add-cart/', views.cart_add, name='add-cart')
]
