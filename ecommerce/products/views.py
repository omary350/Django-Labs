from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product.html', {'product': product})

def products(request):
    # products = Product.objects.all()
    products = Product.objects.filter(active=True)
    return render(request, 'products/products.html', {'products': products})