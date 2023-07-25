from django.shortcuts import render

from common.models import Customer, Seller
from seller.models import Product


def approve_sellers(request):
    return render(request, 'ecom_admin/approve sellers.html')


def ecom_home(request):
    customer_count = Customer.objects.count()
    seller_count = Seller.objects.count()
    product_count = Product.objects.count()
    return render(request, 'ecom_admin/home.html', {'c_count': customer_count,'s_count': seller_count,'p_count':product_count})


def view_customers(request):
    customers = Customer.objects.all()
    return render(request, 'ecom_admin/view customers.html',{'customers':customers})


def view_sellers(request):
    sellers = Seller.objects.all()
    return render(request, 'ecom_admin/view sellers.html',{'sellers':sellers})


def view_orders(request):
    return render(request, 'ecom_admin/view orders.html')


def recent_updates(request):
    return render(request, 'ecom_admin/recent updates.html')


def view_products(request):
    return render(request, 'ecom_admin/view products.html')


def remove_customer(request):
    return render(request, 'ecom_admin/remove customer.html')


def remove_seller(request):
    return render(request, 'ecom_admin/remove seller.html')


def remove_product(request):
    return render(request, 'ecom_admin/remove product.html')


def admin_master(request):
    return render(request, 'ecom_admin/admin_master.html')
