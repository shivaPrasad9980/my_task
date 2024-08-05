from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
from rest_framework.generics import ListAPIView,UpdateAPIView
from testapp.api.serializers import ProductSerializer
from .models import Product
from .cart import add_to_cart, adjust_quantity
from django.views.decorators.http import require_POST
from .cart import get_cart

# Create your views here.



@require_POST
def update_cart(request):
    
    action = request.POST.get('action')
    sku = request.POST.get('sku')
    quantity = int(request.POST.get('quantity', 1))

    if not sku or quantity < 0:
        return HttpResponseBadRequest("Invalid SKU or quantity.")

    try:
        if action == 'add':
            add_to_cart(request, sku, quantity)
        elif action == 'adjust':
            adjust_quantity(request, sku, quantity)
        else:
            return HttpResponseBadRequest("Invalid action.")
    except ValueError as e:
        return HttpResponseBadRequest(str(e))

    return render('cart_summary.html')




def cart_summary(request):
    
    cart = get_cart(request)
    
    # Calculate total price
    total_price = sum(float(item['price']) * item['quantity'] for item in cart.values())
    
    return render(request, 'cart_summary.html', {'cart': cart, 'total_price': total_price})

