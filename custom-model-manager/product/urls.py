from django.contrib import admin
from django.urls import path
from .views import product_add, product_list, active_product_list, expensive_product_list 
urlpatterns = [
    path('add', product_add, name="product_list"),
    path('all', product_list, name="product_list"),
    path('active', active_product_list, name="product_list"),
    path('expensive', expensive_product_list, name="product_list"),
    
]
