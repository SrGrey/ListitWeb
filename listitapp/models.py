from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model

# Create your models here.
class Products(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)    
    product_name = models.CharField(max_length=25,  db_index=True,  default='new product',
                                    verbose_name='Product')
    price = models.FloatField(null=True, blank=True, default=0.0, verbose_name='Price')
    quantity = models.FloatField(null=True, blank=True, default=0,
                                    verbose_name='Quantity')
    total_price = models.FloatField(null=True, blank=True, default=0.0, verbose_name='Total')
    product_status = models.BooleanField(null=True, blank=True,  default=False,
                                    verbose_name='In cart')
    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.CASCADE, verbose_name='Category') #on_delete=models.PROTECT - if we want prohib cascade deleting


    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
        ordering = ['product_status', 'product_name']


    def __str__(self): 
        return self.product_name


    @property 
    def total_cost(self): 
        return round((self.quantity * self.price), 2)


class Category(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=30, verbose_name='Category')
    is_published = models.BooleanField(default=False, verbose_name='Show')
#    users_list = models.ManyToManyField(Users_List, blank=True, related_name='cats')
#    products = models.ForeignKey('Products', null=True,  db_index=True,
#                                on_delete=models.CASCADE, verbose_name='Products') )
#    id = models.AutoField(primary_key=True)


    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        ordering = ['name', 'is_published']


    def __str__(self): 
        return self.name


# class Users_List(models.Model):
#     list_name = models.CharField(max_length=20,
#                             verbose_name='List name')
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     category = models.ManyToManyField(Category, blank=True, related_name='cats')
#
#     class Meta:
#         verbose_name_plural = "User's lists"
#         verbose_name = "User's list"
#         ordering = ['list_name']
#
#
#     def __str__(self):
#         return self.list_name

