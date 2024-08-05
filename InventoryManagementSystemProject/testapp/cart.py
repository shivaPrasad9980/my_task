from django.shortcuts import get_object_or_404
from .models import Product  

def get_cart(request):
   
    cart = request.session.get('cart', {})
    return cart

def save_cart(request, cart):
   
    request.session['cart'] = cart
    request.session.modified = True

def add_to_cart(request, sku, quantity):
    
    cart = get_cart(request)
    product = get_object_or_404(Product, sku=sku)
    
    if sku in cart:
        cart[sku]['quantity'] += quantity
    else:
        cart[sku] = {
            'product_id': product.id,
            'sku': product.sku,
            'name': product.name,
            'price': str(product.price),  
            'quantity': quantity
        }
    
    save_cart(request, cart)

def adjust_quantity(request, sku, quantity):
    
    cart = get_cart(request)
    
    if sku in cart:
        if quantity <= 0:
            del cart[sku]
        else:
            cart[sku]['quantity'] = quantity
        save_cart(request, cart)
    else:
        raise ValueError("Item not in cart.")
