# mart/urls.py

from django.urls import path
from .views import *

# api import
from .api import *

urlpatterns = [
    path('', products, name='products'),
    path('product/', product, name='product'),
    path('product/<int:product_id>/', product, name='product'), 
    
    
    # api routes
    path('api/products/', products_api, name='products_api'),
    path('api/product/<int:product_id>/', product_api, name='product_api'),
]
