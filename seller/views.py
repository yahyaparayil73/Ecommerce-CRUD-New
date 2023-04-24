from django.shortcuts import redirect, render
from common.models import Seller
from seller.decorators import auth_seller
from seller.models import Product
from django.http import JsonResponse


@auth_seller
def add_product(request):
    msg = ''
    if request.method == 'POST':
        pname = request.POST['p_name']
        pdescription = request.POST['p_description']
        pcategory = request.POST['p_category']
        pnumber = request.POST['p_number']
        pstock = request.POST['p_current_stock']
        pprice = request.POST['p_price']
        pimage = request.FILES['p_image']
        new_product = d(
            p_name=pname,
            p_description=pdescription,
            p_category=pcategory,
            p_number=pnumber,
            p_stock=pstock,
            p_price=pprice,
            p_image=pimage,
            seller_id=request.session['seller']
        )

        new_product.save()
        msg = 'Product added successfully'

    return render(request, 'seller/add product.html', {'success_message': msg})


@auth_seller
def change_password(request):
    msg = ''
    if request.method == 'POST':
        oldpassword = request.POST['old_password']
        newpassword = request.POST['new_password']
        seller = Seller.objects.get(id=request.session['seller'])
        if seller.s_password == oldpassword:
            seller.s_password = newpassword
            seller.save()
            msg = 'password updated'
        else:
            msg = 'password does not match'
    return render(request, 'seller/change password.html', {'password_message': msg})


@auth_seller
def seller_home(request):
    seller = Seller.objects.get(id=request.session['seller'])
    return render(request, 'seller/seller home.html', {'seller_data': seller})


def product_catalogue(request):
    return render(request, 'seller/product catalogue.html')


@auth_seller
def seller_profile(request):
    seller = Seller.objects.get(id=request.session['seller'])
    return render(request, 'seller/seller profile.html', {'seller_profile_data': seller})

@auth_seller
def update_stock(request):
    products = Product.objects.filter(
        seller=request.session['seller']).values('id', 'p_name')
    if request.method == 'POST':
        prodnum = request.POST['p_number']
        new_stock = request.POST['new_stock']
        product1 = Product.objects.get(id=prodnum)
        product1.p_stock += int(new_stock)
        product1.save() 

    return render(request, 'seller/update stock.html', {'products': products})

@auth_seller
def view_product(request):
    sellerid = request.session['seller']
    product = Product.objects.filter(seller_id=sellerid)
    return render(request, 'seller/view_product.html', {'product_message': product})

@auth_seller
def view_orders(request):
    return render(request, 'seller/view orders.html')

@auth_seller
def master_seller(request):
    return render(request, 'seller/master_seller.html')

def seller_logout(request):
    del request.session['seller']
    request.session.flush()
    return redirect('common:project_home')

def stock_update(request):
    product_id = request.POST['product_id']
    product = Product.objects.filter(id=product_id).values('p_stock')
    current_stock = product[0]['p_stock']
    return JsonResponse({'stock': current_stock})
