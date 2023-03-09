from django.urls import path
from . import views
app_name='customer'
urlpatterns=[
    path('customer_home',views.customer_home,name='home'),
    path('ccheckout',views.customer_checkout,name='checkout'),
    path('cmycart',views.customer_mycart,name='mycart'),
    path('cchangepassword',views.customer_changepassword,name='changepassword'),
    path('cproductdetails',views.customer_productdetails,name='productdetails'),
    path('cprofile',views.customer_profile,name='customer_profile'),
    path('cmyorders',views.customer_myorders,name='myorders'),
    path('cbaabtrawebsite',views.customer_Baabtrawebsite,name='Baabtra website'),
    path('cbootstrap',views.customer_Bootstrap,name='Bootstrap'),
    path('cbootstrapgrid',views.customer_Bootstrapgrid,name='bootstrapgrid'),
    path('cjavascripttest',views.customer_Javascripttest,name='javascripttest'),
    path('cvariable',views.customer_variable,name='variable'),
    path('cdomsample',views.customer_domsample,name='domsample'),
    path('cToDo',views.customer_ToDo,name='ToDo'),
    path('cProductDetail',views.customer_ProductDetail,name='Productdetail'),
    path('cjquerysample',views.customer_jquerysample,name='jquerysample'),
    path('cjquerysample2',views.customer_jquerysample2,name='jquerysample2'),
    path('cjquerysample2',views.customer_jquerysample2,name='jquerysample2'),
    path('cformname',views.customer_formname,name='formname'),
    path('clistsample',views.customer_listsample,name='listsample'),
    path('carraysample',views.customer_arraysample,name='arraysample'),
    path('cinnerwidthsample',views.customer_innerwidthsample,name='innerwidthsample'),
    path('cjqueryvalidation',views.customer_jqueryvalidation,name='jqueryvalidation'),
    path('cminitodolist',views.customer_minitodolist,name='minitodolist'),
    path('ccustomerregistration',views.customer_customerregistration,name='customerregistration'),
    path('ccssgrid',views.customer_cssgrid,name='cssgrid'),
    path('css_broto_sample',views.css_broto_sample,name='css_broto_sample'),


]