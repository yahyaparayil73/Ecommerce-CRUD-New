from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from common.models import Customer
from .models import Cart
from seller.models import Product
from .decorators import auth_customer
import logging

logger = logging.getLogger('django')

@auth_customer
def customer_home(request):
    customer = Customer.objects.get(id = request.session['customer'])
    products = Product.objects.all()
    return render(request,'customer/customer_home.html',{'customer_data':customer,'product_data':products})

def customer_checkout(request):
    return render(request,'customer/checkout.html')

@auth_customer
def customer_mycart(request):
    cart_items = Cart.objects.filter(customer = request.session['customer'])  
    # print(cart_items) 
    return render(request,'customer/my cart.html',{'cart_items': cart_items})

def customer_myorders(request):
    return render(request,'customer/my orders.html')

@auth_customer
def customer_productdetails(request,p_id):
    product = Product.objects.get(id = p_id)
    msg = ''
    if request.method == 'POST':
        cart_exist = Cart.objects.filter(
            product = p_id, 
            customer = request.session['customer']).exists()

        if not cart_exist:
            cart = Cart(customer_id = request.session['customer'], product_id = p_id)
            cart.save() 
            return redirect('customer:mycart')
        else:
            msg = 'Item already in cart'
    return render(request,'customer/product details.html',{'product':product,'msg':msg})
    
@auth_customer
def customer_changepassword(request):
    msg = ''
    if request.method == "POST" :
        oldpassword = request.POST['old_password']
        newpassword = request.POST['new_password']
        customer = Customer.objects.get(id = request.session['customer'])
        if customer.c_password == oldpassword :
            customer.c_password = newpassword
            customer.save()
            msg = 'Password Updated'
        else:
            msg = 'Passwords does not match'

    return render(request,'customer/change password.html',{'message':msg})

@auth_customer
def customer_profile(request):
    
    customer = Customer.objects.get(id = request.session['customer'])
    return render(request, 'customer/customer_profile.html',{'customer_profile':customer})  

def master_customer(request):
    return render(request, 'customer/master_customer.html')  

def customer_logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect( 'common:project_home')

def change_quantity(request):
    error_msg = ''
    quantity = int(request.POST['quantity'])
    product_id = int(request.POST['product_id'])
    current_stock = Product.objects.get(id = product_id).p_stock
    if quantity > current_stock :
        error_msg = 'Out of stock'
    else:
        error_msg = 'In stock'
    return JsonResponse({'error_msg': error_msg})

def info(request):
    logger.warning('this is  a warning message')
    a = 10
    b = 0
    try:
        c = a/b
    except Exception as e:
        logger.error('Exception has occured',exc_info = True)
    return HttpResponse('Exception message')