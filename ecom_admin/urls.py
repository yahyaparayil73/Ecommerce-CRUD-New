from django.urls import path
from .import views
app_name='ecom_admin'


urlpatterns = [
    path('approve sellers',views.approve_sellers,name='approve sellers'),
    path('ecom home',views.ecom_home,name='ecom home'),
    path('view customers',views.view_customers,name='view customers'),
    path('view sellers',views.view_sellers,name='view sellers'),
    path('view orders',views.view_orders,name='view orders'),
    path('recent updates',views.recent_updates,name='recent updates'),
    path('view products',views.view_products,name='view products'),
    path('remove customer',views.remove_customer,name='remove customer'),
    path('remove seller',views.remove_seller,name='remove seller'),
    path('remove product',views.remove_product,name='remove product'),
    

]