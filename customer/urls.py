from django.urls import path
from . import views
app_name='customer'
urlpatterns=[
    path('customer_home',views.customer_home,name='home'),
    path('ccheckout',views.customer_checkout,name='checkout'),
    path('cmycart',views.customer_mycart,name='mycart'),
    path('cchangepassword',views.customer_changepassword,name='changepassword'),
    path('cproductdetails/<int:p_id>',views.customer_productdetails,name='productdetails'),
    path('cprofile',views.customer_profile,name='customer_profile'),
    path('cmyorders',views.customer_myorders,name='myorders'),
    path('ccustomerregistration',views.customer_customerregistration,name='customerregistration'),
    path('c_logout',views.customer_logout,name='customer_logout'),
    path('master_customer',views.master_customer,name='master_customer'),
    path('change_quantity',views.change_quantity,name ='change_quantity')

]