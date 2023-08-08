from django.db import models

from common.models import Customer
from seller.models import Product

# Create your models here.

class Cart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    
  
    class Meta:
        db_table = 'cart'

class Orders(models.Model):
    cart = models.ForeignKey(Cart,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_id = models.CharField(max_length = 100)
    ordered_date = models.DateTimeField(auto_now_add=True)
    pincode = models.IntegerField()
    phone = models.BigIntegerField()
    address = models.CharField(max_length = 100)
    place = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        db_table = 'orders'
