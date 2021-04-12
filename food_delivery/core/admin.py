from django.contrib import admin
from .models import (
    Store,
    Product,
    Category,
    ProductCategory,
    Stock,
    Order,
    OrderDetail,
    Cart,
    CustomerShippingAddress,
    StoreProfile
)
# Register your models here.

admin.site.register(Store)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(ProductCategory)
admin.site.register(Stock)
admin.site.register(Order)
admin.site.register(OrderDetail)
admin.site.register(Cart)
admin.site.register(CustomerShippingAddress)
admin.site.register(StoreProfile)
