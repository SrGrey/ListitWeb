from django.contrib import admin

# Register your models here.
from .models import Products
from .models import Category

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'quantity', 'total_price', 'product_status', 'category')
    list_display_links = ('product_name', 'price', 'quantity', 'total_price', 'product_status')
    search_fields = ('product_name', 'product_status')

admin.site.register(Products, ProductsAdmin)
admin.site.register(Category)