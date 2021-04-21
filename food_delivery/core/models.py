from django.db import models
from django.urls import reverse
from django.utils.text import slugify

from PIL import Image

from user.models import Customer
# Create your models here.
class Store(models.Model):
    store_help_text = 'Keep in mind you can only own one store at the moment'

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=250, help_text=store_help_text)
    location = models.CharField(max_length=500)
    slug = models.SlugField(blank=True, max_length=500)

    def __str__(self):
        return self.store_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.slug = slugify(self.store_name)

    def get_absolute_url(self):
        return reverse('core:store-page', args=[self.slug])

class StoreProfile(models.Model):
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
    store_profile = models.ImageField('Store profile photo', upload_to='store/profile', blank=True)
    store_cover = models.ImageField('Store cover photo', upload_to='store/cover', blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.store_profile)

        if img.width > 300 or img.height > 300:
            profile_size = (300, 300)
            img.thumbnail(profile_size)
            img.save(self.store_profile.path)

    def __str__(self):
        return f'{self.store.store_name} store'

class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(blank=True, max_length=500)
    price = models.CharField(max_length=250)
    description = models.TextField(max_length=1000)
    create_date = models.DateTimeField()
    thumbnail = models.ImageField(upload_to='uploads')
    weight = models.DecimalField(max_digits=5, decimal_places=2, default=0, help_text='in kg')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.slug = slugify(self.name)
        # img = Image.open(self.thumbnail)

        # if img.width > 300 or img.height > 300:
            # output = (300, 300)
            # img.thumbnail(output)
            # img.save(self.thumbnail.path)


class Category(models.Model):
    name = models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class ProductCategory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.product.name

    def get_absolute_url(self):
        return reverse('core:product-page', args=[self.product.store.slug, self.product.slug])

    class Meta:
        verbose_name_plural = 'Products has Categories'

class Stock(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    store = models.OneToOneField(Store, on_delete=models.CASCADE)
    quantity = models.IntegerField()


    def __str__(self):
        if self.quantity <= 0:
            return f'{self.product.name} is out of stock'
        return f'{self.product.name} has stock'

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)


    def __str__(self):
        return f'{self.customer.get_fullname} cart'

class CustomerShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=400, blank=True)
    phone = models.IntegerField()
    house_no = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=15)
    province = models.CharField(max_length=60)
    city_municipality = models.CharField(max_length=80)
    barangay = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.customer.get_fullname} address'

    class Meta:
        verbose_name_plural = 'Customer\'s Shipping Addresses'

class Order(models.Model):
    STATUS = [
        ('Pending', 'Pending'),
        ('Ready to Pickup', 'Ready to Pickup'),
        ('On its way', 'On its way'),
        ('Delivered', 'Delivered')
    ]

    customer = models.ForeignKey(CustomerShippingAddress, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    order_status = models.CharField(max_length=20, choices=STATUS)

    def __str__(self):
        return f'{self.customer.customer.get_fullname} order'

class OrderDetail(models.Model):
    OPTIONS = [
        ('Pickup',  'Pickup'),
        ('Online Payment', 'Online Payment'),
        ('COD', 'COD')
    ]

    order = models.OneToOneField(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    options = models.CharField(max_length=25, choices=OPTIONS)

    def __str__(self):
        return f'{self.order.customer.customer.get_fullname} order detail'

