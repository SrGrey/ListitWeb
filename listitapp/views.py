from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Products, Category

DEFAULT_USER_ID = 7


def index(request):
    return render(request, 'listitapp/index.html')


def shopping_list(request):
    prods = Products.objects.order_by('category', 'product_status', 'product_name').filter(user=request.user)
    users_categories = Category.objects.order_by('name').filter(user=request.user)
    categories = users_categories
    context = {
        'prods': prods,
        'categories': categories,
    }
    return render(request, 'listitapp/shopping_list.html', context)


def actual_list(request):
    prods = Products.objects.order_by('category', 'product_status', 'product_name').filter(user=request.user).filter(
        is_published=True)
    users_categories = Category.objects.order_by('name').filter(user=request.user)
    categories = users_categories
    context = {
        'prods': prods,
        'categories': categories,
    }
    return render(request, 'listitapp/actual_list.html', context)


def create_category(request):
    if request.method == "POST":
        new_category = Category()
        new_category.name = request.POST['new_category']
        new_category.user = request.user
        new_category.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def create_product(request, pk):
    if request.method == "POST":
        category = Category.objects.get(id=pk)
        new_product = Products()
        new_product.category = category
        new_product.user = request.user
        new_product.product_name = request.POST['new_product']
        new_product.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def modify_product(request, pk):
    #    if request.method == "POST":
    #       category = Category.objects.get(id=pk)
    #       new_product = Products()
    #       new_product.category = category
    #       new_product.product_name = request.POST['new_product']
    #       new_product.save()
    return HttpResponseRedirect('/shopping_list')


###AJAX POST price/cuantity/total QUERY
@csrf_exempt
def calculate_total(request, pk):
    if request.method == "POST" and request.is_ajax():
        request_price = float(request.POST.get('price', None))
        request_quantity = float(request.POST.get('quantity', None))
        product = Products.objects.get(id=pk)
        product.price = request_price
        product.quantity = request_quantity
        product.save()
        print(product.total_cost)
        context = {
            'price': product.price,
            'quantity': product.quantity,
            'total_cost': product.total_cost
        }
    return JsonResponse(context)


def modify_product_status(request, pk):
    product = Products.objects.get(id=pk)
    product.product_status = not product.product_status
    product.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_category(request, pk):
    category_to_delete = Category.objects.get(id=pk)
    category_to_delete.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def hide_category(request, pk):
    category_to_hide = Category.objects.get(id=pk)
    category_to_hide.is_published = False
    category_to_hide.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def show_category(request, pk):
    category_to_hide = Category.objects.get(id=pk)
    category_to_hide.is_published = not category_to_hide.is_published
    category_to_hide.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def hide_product(request, pk):
    product_to_hide = Products.objects.get(id=pk)
    product_to_hide.is_published = False
    product_to_hide.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def show_product(request, pk):
    product_to_hide = Products.objects.get(id=pk)
    product_to_hide.is_published = not product_to_hide.is_published
    product_to_hide.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def delete_product(request, pk):
    product_to_delete = Products.objects.get(id=pk)
    product_to_delete.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# def pageNotFound(request, exception):
#     return HttpResponseNotFound('<h1>Page not found</h1><a href="/">main page</a>')

def login_form(request):
    return render(request, 'listitapp/login.html')  # accounts/login.html


def add_default_categories(request):
    common_categories = Category.objects.order_by('name').filter(user=DEFAULT_USER_ID)
    users_category = Category.objects.filter(user=request.user)
    users_category_names = [item.name for item in users_category]
    for category in common_categories:
        if category.name not in users_category_names:
            new_category = Category()
            new_category.name = category.name
            new_category.user = request.user
            new_category.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
