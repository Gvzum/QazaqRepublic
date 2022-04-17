from django.db import models
from django.contrib.auth.models import User  # Importing User model from auth app


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.user.username if self.user else self.name


class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name', )
        verbose_name = 'category'
        verbose_name_plural = 'categories'


class Color(models.Model):
    name = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


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
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=True)
    transaction = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_basket_amount(self):
        basket_order_items = self.orderitem_set.all()
        return sum([item.quantity * item.product.price for item in basket_order_items])

    @property
    def get_basket_total(self):
        basket_order_items = self.orderitem_set.all()
        return sum([item.quantity for item in basket_order_items])


class OrderItem(models.Model):

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

    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    size = models.CharField(choices=CLOTHES_SIZE, default=None, max_length=10)


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, blank=True, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name