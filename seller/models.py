from django.db import models
from common.models import Seller

# Create your models here.


class Product(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    p_name = models.CharField(max_length=50)
    p_description = models.CharField(max_length=50)
    p_number = models.BigIntegerField()
    p_stock = models.BigIntegerField()
    p_price = models.BigIntegerField()
    p_category = models.CharField(max_length=50)
    p_image = models.ImageField(upload_to='product/')

    class Meta:
        db_table = 'product'
