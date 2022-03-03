from django.contrib.auth.models import User
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'

class Product(models.Model):
    slug = models.SlugField(unique=True, max_length=200)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    first_photo = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Favors(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    # Cloth size tuples
    XSMALL = 'XS'
    SMALL = 'S'
    MEDIUM = 'M'
    LARGE = 'L'
    XLARGE = 'XL'
    XXLARGE = 'XXL'
    CLOTHES_SIZE = [
        (XSMALL, 'extra small'),
        (SMALL, 'small'),
        (MEDIUM, 'medium'),
        (LARGE, 'large'),
        (XLARGE, 'extra large'),
        (XXLARGE, 'extra extra large'),
    ]

    # State of ordering tuples
    BASKET = 'B'
    ORDER = 'O'
    ORDER_TYPE = [
        (BASKET, 'basket'),
        (ORDER, 'order')
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=2, decimal_places=2)
    size = models.CharField(choices=CLOTHES_SIZE, default=None, max_length=10)
    state = models.CharField(choices=ORDER_TYPE, default=BASKET, max_length=10)