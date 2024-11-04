from django.shortcuts import render
from .models import Product

def home(request):
    return render(request, 'app_58/home.html')

def product_list(request):
    products = Product.objects.all()
    return render(request, 'app_58/product_list.html', {'products': products})
