from django.db import models

# Create your models here.

# class Customers(models.Model):
#     name = models.CharField(max_length=50)
#     mobile_number = models.CharField(max_length=20)
#     email = models.CharField(max_length=30)
#     password = models.CharField(max_length=20)
    
#     class Meta: 
#         db_table = 'customer_tb'


# class Seller(models.Model):
#     name = models.CharField(max_length=50) 
#     mobile_number = models.BigIntegerField()
#     email = models.CharField(max_length=30)
#     password = models.CharField(max_length=20)
#     user_name = models.IntegerField(default=0)
#     bank_name = models.CharField(max_length=30)
#     bank_branch = models.CharField(max_length=40)
#     ifsc_code = models.CharField(max_length=20)
#     seller_pic = models.ImageField(upload_to='seller/')

#     class Meta:
#         db_table = 'seller_tb'

class Customer(models.Model) :
    c_name = models.CharField(max_length = 50)
    c_email = models.CharField(max_length = 50)
    c_address = models.CharField(max_length = 100)
    c_mobile = models.BigIntegerField()
    c_gender = models.CharField(max_length = 10)
    c_password = models.CharField(max_length = 30, default = '')
    c_status = models.CharField(max_length = 25, default = 'active')
        
    class Meta : 
        db_table = 'customer'

class Seller(models.Model) :
    s_name = models.CharField(max_length = 50)
    s_email = models.CharField(max_length = 50)
    s_address = models.CharField(max_length = 100)
    s_mobile = models.BigIntegerField()
    s_username = models.IntegerField(default = 0)
    s_password = models.CharField(max_length = 50)
    s_bank_name = models.CharField(max_length = 50)
    s_bank_branch = models.CharField(max_length = 50)
    s_ifsc_code = models.CharField(max_length = 50)
    s_acc_number = models.BigIntegerField()
    s_image = models.ImageField(upload_to = 'seller/')
    s_status = models.CharField(max_length = 20, default = 'pending')

    class Meta : 
        db_table = 'seller'

    