from django.urls import path
from . import views
app_name = 'common'

urlpatterns = [
    path('comadminlogin', views.admin_login, name='admin_login'),
    path('customerlogin', views.customer_login, name='customer_login'),
    path('customersignup', views.customer_signup, name='customer_signup'),
    path('projecthome', views.project_home, name='project_home'),
    path('sellerlogin', views.seller_login, name='seller_login'),
    path('sellersignup', views.seller_signup, name='seller_signup'),
    path('mastercommon', views.master_common, name='master_common'),
    path('test', views.test, name='test'),


]
