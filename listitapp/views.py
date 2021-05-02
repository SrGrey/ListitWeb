from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.template import loader

from .models import Products, Category

# Create your views here.
def index(request):

#    s = 'The product\'s list\r\n\r\n\r\n'
#    for product in Products.objects.order_by('product_name'):
#        s += product.product_name + ' - - - ' + str(product.total_price) + '\r\n'
#    return HttpResponse(s, content_type='text/plain; charset=utf-8')

 #   template = loader.get_template('listitapp/index.html')
 #   prods = Products.objects.order_by('product_name', 'product_status')
 #   context = {'prods': prods}
 #   return HttpResponse(template.render(context,request))
    prods = Products.objects.order_by('category', 'product_status', 'product_name')
    categories = Category.objects.order_by('name')
 #   total_sum = prods.price #Products.quantity #Products.objects.get(product_name) 
    context = {
        'prods': prods,
        'categories': categories,
 #       'total_sum': product.price ,
    }
    return render(request, 'listitapp/index.html', context)

def create_category(request):
#       new_category_name = ''
    if request.method == "POST":
    #   new_category = request.POST.get()
       new_category = Category()
       new_category.name = request.POST['new_category']
       new_category.save()
    return  HttpResponseRedirect('/listitapp/')