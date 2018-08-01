from django.db import models
import datetime
from django.utils import timezone


class Customer(models.Model):
    first = models.CharField(max_length=120)
    last = models.CharField(max_length=120)
    date_created = models.DateTimeField(default='')
    expiration_date = models.DateTimeField(default='')
    active = models.BooleanField(default=False)

    class Meta:
        db_table = 'customer'

class ProductType(models.Model):
    category = models.CharField(max_length=100)

    class Meta: 
        db_table = 'product_type'

class Product(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_type_id = models.ForeignKey(ProductType, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    title = models.TextField(default="")
    description = models.TextField(default="")

    class Meta:
        db_table = 'product'

class PaymentType(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    account_number = models.IntegerField(default="10")

    class Meta:
        db_table = 'payment_type'

class Orders(models.Model):
    customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.CASCADE)

    class Meta:
        db_table = 'orders'