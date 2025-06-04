from django.core.serializers import serialize
from django.shortcuts import render
from django.http import JsonResponse


from product.models import Product

# Create your views here.

def add_sample_product():
    prodcut_list = [
        # active
        {"id": "1", "name": "Laptop",    "price": 50000, "is_active": True},
        {"id": "2", "name": "Monitor",   "price": 4000, "is_active": True},
        {"id": "3", "name": "Keyboard",  "price": 1500, "is_active": True},
        {"id": "4", "name": "Mouse",     "price": 800, "is_active": True},
        {"id": "5", "name": "HeadPhone", "price": 3000, "is_active": True},
        # in-active
        {"id": "6", "name": "Desck Chair", "price": 5000, "is_active": False},
        {"id": "7", "name": "Desck Lamp",  "price": 800,  "is_active": False},
    ]
    for prodcut in prodcut_list:
        Product.objects.update_or_create(
            id=prodcut["id"],
            defaults={
                "name": prodcut["name"],
                "price": prodcut["price"],
                "is_active": prodcut["is_active"]
            }
        )
    print("Product added successfully.")
    
def product_add(request):
    add_sample_product()
    products = Product.objects.all().values()
    return JsonResponse(list(products), safe=False)
    
def product_list(request):
    products = Product.objects.all().values()
    return JsonResponse(list(products), safe=False)
    
def active_product_list(request):
    products = Product.active.all().values()
    return JsonResponse(list(products), safe=False)

def expensive_product_list(request):
    products = Product.active.expensive(threshold=1000).values()
    return JsonResponse(list(products), safe=False)