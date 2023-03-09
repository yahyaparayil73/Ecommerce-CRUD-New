from django.conf import settings
from django.shortcuts import render,redirect
from random import randint
from .models import Customer, Seller
from django.core.mail import send_mail


def admin_login(request):
    return render(request, 'common/admin login.html')


def customer_login(request):

    msg = ''
    if request.method == 'POST':
        cemail = request.POST['email']
        cpassword = request.POST['password']
        try :
            customer = Customer.objects.get(c_email = cemail,c_password = cpassword)
            request.session['customer'] = customer.id
            return redirect('customer:home')

        except:
            msg = 'invalid credentials'
    
    return render(request, 'common/customer login.html',{'message':msg})


def customer_signup(request):
    msg = ''

    if request.method == 'POST' :
        cname = request.POST['customer_name']
        cemail = request.POST['email']
        cmobile = request.POST['mobile_number']
        caddress = request.POST['address']
        cgender = request.POST['gender']
        cpassword = request.POST['password']

        try:
            new_customer = Customer(
                c_name = cname, 
                c_email = cemail, 
                c_mobile = cmobile,
                c_address = caddress, 
                c_gender = cgender,
                c_password = cpassword
                )
            new_customer.save()
            msg = 'successfully registered'
        except:
            msg = 'invalid credentials'


    return render(request, 'common/customer signup.html', {'message':msg})


def project_home(request):
    return render(request, 'common/project home.html')


def seller_login(request):
    msg = ''

    if request.method == 'POST' :

        susername = request.POST['username']
        spassword = request.POST['password']
        try:
            seller = Seller.objects.get(s_username=susername, s_password = spassword)
            return redirect('seller:seller_home')
        except:
            msg = 'Invalid Credentials'
    return render(request, 'common/seller login.html',{'message':msg})


def seller_signup(request):
    msg = ''
    if request.method == 'POST' :
        sname = request.POST['seller_name']
        smobile = request.POST['seller_mobile']
        semail = request.POST['seller_email']
        saddress = request.POST['seller_address']
        sbankname = request.POST['seller_bank_name']
        saccountnumb = request.POST['seller_account_number']
        sbankbranch = request.POST['seller_bank_branch']
        sifsccode = request.POST['seller_ifsc']
        simage = request.FILES['seller_pic']
        susername = randint(1000,9999)
        spassword = 'sel-'+sname.lower()+str(susername)

        seller = Seller(
            s_name = sname,
            s_mobile = smobile,
            s_email = semail,
            s_address = saddress,
            s_bank_name = sbankname,
            s_acc_number = saccountnumb,
            s_bank_branch = sbankbranch,
            s_ifsc_code = sifsccode,
            s_image = simage,
            s_username = susername,
            s_password = spassword)
        seller.save()
        
        msg = 'seller registered successfully'

        subject = 'account name and password'
        message = 'hai your username is '+str(susername)+'and your password is '+spassword
        email_from = settings.EMAIL_HOST_USER
        send_mail(
            subject,
            message,
            email_from,
            [semail],
            fail_silently = False
        )
        
    return render(request, 'common/seller signup.html',{'message':msg})

def master_common(request):
    return render(request, 'common/master_common.html')         

def test(request):
    return render(request, 'common/test.html')

    

     
