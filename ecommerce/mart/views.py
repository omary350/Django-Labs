from django.shortcuts import render, redirect

# Product list
products = [
    {"id": 1, "name": "Product A", "price": 10.99},
    {"id": 2, "name": "Product B", "price": 15.49},
    {"id": 3, "name": "Product C", "price": 7.99},
]
def index(request):
    if request.method == 'POST':
        selected_product_ids = request.POST.getlist('selected_products')
        selected_products = [product for product in products if str(product["id"]) in selected_product_ids]
        
        print('Selected Products:', selected_products)
        print('Selected Product IDs:', selected_product_ids)
        
        query_string = '&'.join([f'product_ids={id}' for id in selected_product_ids])
        return redirect(f'show/?{query_string}')
    
    return render(request, 'mart/index.html', {'products': products})

def show(request):
    selected_product_ids = request.GET.getlist('product_ids')
    
    print('Retrieved Selected Product IDs:', selected_product_ids)
    
    selected_products = [product for product in products if str(product["id"]) in selected_product_ids]
    
    print('Filtered Selected Products:', selected_products)
    
    return render(request, 'mart/show.html', {'selected_products': selected_products})