from django.contrib import admin

# Register your models here.
from .models import Products
from .models import Category
# from .models import Users_List

class ProductsAdmin(admin.ModelAdmin):
    list_display = ('product_name', 'price', 'quantity', 'total_price', 'product_status', 'category', 'id', 'user')
    list_display_links = ('product_name', 'price', 'quantity', 'total_price', 'product_status')
    search_fields = ('product_name', 'product_status')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published', 'id', 'user')
    list_display_links = ('name', 'is_published','id',)

# class Users_ListAdmin(admin.ModelAdmin):
#     list_display = ('list_name', 'id',)
#     list_display_links = ("list_name", 'id',)


admin.site.register(Products, ProductsAdmin)
admin.site.register(Category, CategoryAdmin)
# admin.site.register(Users_List, Users_ListAdmin)