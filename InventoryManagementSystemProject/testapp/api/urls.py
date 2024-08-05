from django.urls import path
from . import views 
from django.urls import path





urlpatterns = [
    path('products/',views.ProductView.as_view(),name="productview"),
    path('products/<str:sku>/',views.ProductUpdateView.as_view(),name = "productUpdate"),
    
]
