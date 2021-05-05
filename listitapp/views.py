from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

from .models import Products, Category


def index(request):
    prods = Products.objects.order_by('category', 'product_status', 'product_name')
    categories = Category.objects.order_by('name')
    context = {
        'prods': prods,
        'categories': categories,
 #       'total_sum': product.price ,
    }
    return render(request, 'listitapp/index.html', context)


def create_category(request):
    if request.method == "POST":
       new_category = Category()
       new_category.name = request.POST['new_category']
       new_category.save()
    return  HttpResponseRedirect('/listitapp/')


def delete_category(request, pk):
    category_to_delete = Category.objects.get(id=pk)
    category_to_delete.delete()
    return HttpResponseRedirect('/')
