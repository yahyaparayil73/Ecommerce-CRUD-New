

from django.shortcuts import redirect


def auth_seller(func):
    def wrapper(request, *args, **kwargs):
        if 'seller' not in request.session :
            return redirect('common:seller_login')
        else:
            return func
    return wrapper