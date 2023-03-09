from django.shortcuts import render


def customer_home(request):
    return render(request,'customer/customer_home.html')

def customer_checkout(request):
    return render(request,'customer/checkout.html')

def customer_mycart(request):
    return render(request,'customer/my cart.html')

def customer_myorders(request):
    return render(request,'customer/my orders.html')

def customer_productdetails(request):
    return render(request,'customer/product details.html')

def customer_changepassword(request):
    return render(request,'customer/change password.html')

def customer_profile(request):
    return render(request, 'customer/customer_profile.html',{'customer_profile':customer_profile}) 

def customer_Baabtrawebsite(request):
    return render(request,'customer/Baabtra website.html') 

def customer_Bootstrap(request):
    return render(request,'customer/Bootstrap.html') 

def customer_Bootstrapgrid(request):
    return render(request,'customer/bootstrapgrid.html') 

def customer_Javascripttest(request):
    return render(request,'customer/javascripttest.html') 

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