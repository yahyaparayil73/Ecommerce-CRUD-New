from django.shortcuts import redirect, render
from common.models import Customer
from .models import Cart
from seller.models import Product


def customer_home(request):
    customer = Customer.objects.get(id = request.session['customer'])
    products = Product.objects.all()
    return render(request,'customer/customer_home.html',{'customer_data':customer,'product_data':products})

def customer_checkout(request):
    return render(request,'customer/checkout.html')

def customer_mycart(request):
     
    cart_items = Cart.objects.filter(customer = request.session['customer'])  
    print(cart_items) 
    return render(request,'customer/my cart.html',{'cart_items': cart_items})

def customer_myorders(request):
    return render(request,'customer/my orders.html')

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

def customer_profile(request):
    customer = Customer.objects.get(id = request.session['customer'])
    return render(request, 'customer/customer_profile.html',{'customer_profile':customer}) 

def customer_Baabtrawebsite(request):
    return render(request,'customer/Baabtra website.html') 

def customer_Bootstrap(request):
    return render(request,'customer/Bootstrap.html') 

def customer_Bootstrapgrid(request):
    return render(request,'customer/bootstrapgrid.html') 

def customer_Javascripttest(request):
    return render(request,'customer/javascripttest.html') 

def master_customer(request):
    return render(request, 'customer/master_customer.html')  

def customer_variable(request):
    return render(request,'customer/variable.html') 

def customer_domsample(request):
    return render(request,'customer/domsample.html') 

def customer_ToDo(request):
    return render(request,'customer/ToDo.html') 

def customer_ProductDetail(request):
    return render(request,'customer/ProductDetail.html') 

def customer_jquerysample(request):
    return render(request,'customer/jquerysample.html') 

def customer_jquerysample2(request):
    return render(request,'customer/jquerysample2.html') 

def customer_formname(request):
    return render(request,'customer/formname.html') 

def customer_listsample(request):
    return render(request,'customer/listsample.html') 

def customer_arraysample(request):
    return render(request,'customer/arraysample.html') 

def customer_innerwidthsample(request):
    return render(request,'customer/innerwidthsample.html') 

def customer_jqueryvalidation(request):
    return render(request,'customer/jqueryvalidation.html')

def customer_minitodolist(request):
    return render(request,'customer/MiniToDoList.html') 

def customer_customerregistration(request):
    return render(request,'customer/customerregistration.html') 

def customer_cssgrid(request):
    return render(request,'customer/cssgrid.html') 

def css_broto_sample(request):
    return render(request,'customer/css_broto_sample.html') 

def customer_logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect( 'common:project_home')