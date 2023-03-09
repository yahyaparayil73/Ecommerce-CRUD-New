from django.shortcuts import render

def approve_sellers(request):
    return render(request,'ecom_admin/approve sellers.html')

def ecom_home(request):
    return render(request,'ecom_admin/home.html')

def view_customers(request):
    return render(request,'ecom_admin/view customers.html')

def view_sellers(request):
    return render(request,'ecom_admin/view sellers.html')

def view_orders(request):
    return render(request,'ecom_admin/view orders.html')

def recent_updates(request):
    return render(request,'ecom_admin/recent updates.html')

def view_products(request):
    return render(request,'ecom_admin/view products.html')

def remove_customer(request):
    return render(request,'ecom_admin/remove customer.html')

def remove_seller(request):
    return render(request,'ecom_admin/remove seller.html')

def remove_product(request):
    return render(request,'ecom_admin/remove product.html')
