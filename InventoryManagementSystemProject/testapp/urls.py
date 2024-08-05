from django.urls import path
from .import views 
from django.urls import path





urlpatterns = [
    path('update-cart/', views.update_cart, name='update_cart'),
    path('cart-summary/', views.cart_summary, name='cart_summary'),
]
