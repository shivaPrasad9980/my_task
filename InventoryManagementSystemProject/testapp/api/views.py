from django.shortcuts import render,redirect
from django.http import HttpResponseBadRequest
from rest_framework.generics import ListAPIView,UpdateAPIView
from testapp.api.serializers import ProductSerializer
from testapp.models import Product
from testapp.cart import add_to_cart, adjust_quantity
from django.views.decorators.http import require_POST
from testapp.cart import get_cart

# Create your views here.
class ProductView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "sku"


