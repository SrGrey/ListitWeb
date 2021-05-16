from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Products, Category



def index(request):

    return render(request, 'listitapp/index.html') 


def shopping_list(request):
    prods = Products.objects.order_by('category', 'product_status', 'product_name')
    categories = Category.objects.order_by('name')
    context = {
        'prods': prods,
        'categories': categories,
 #       'total_sum': product.price ,
    }
    return render(request, 'listitapp/shopping_list.html', context)




def create_category(request):
    if request.method == "POST":
       new_category = Category()
       new_category.name = request.POST['new_category']
       new_category.save()
    return  HttpResponseRedirect('/listitapp/shopping_list')


def create_product(request, pk):
    if request.method == "POST":    
       category = Category.objects.get(id=pk)
       new_product = Products()

       new_product.category = category
       new_product.product_name = request.POST['new_product']
#       new_product.category = Category.objects.get(id="id")       

       #new_product.category = request.POST['category']
       new_product.save()
    return  HttpResponseRedirect('/listitapp/shopping_list')


def delete_category(request, pk):
    category_to_delete = Category.objects.get(id=pk)
    category_to_delete.delete()
    return HttpResponseRedirect('/listitapp/shopping_list')


def hide_category(request, pk):
    category_to_hide = Category.objects.get(id=pk)
    category_to_hide.is_published = False
    category_to_hide.save()
    return HttpResponseRedirect('/listitapp/shopping_list')

def delete_product(request, pk):
    product_to_delete = Products.objects.get(id=pk)
    product_to_delete.delete()
    return HttpResponseRedirect('/listitapp/shopping_list')

