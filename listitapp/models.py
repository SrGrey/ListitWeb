from django.db import models

# Create your models here.
class Products(models.Model):

    

    product_name = models.CharField(max_length=25,  db_index=True, 
                                    verbose_name='Product')
    price = models.FloatField(null=True, blank=True, default=0.0, verbose_name='Price')
    quantity = models.FloatField(null=True, blank=True, default=0,
                                    verbose_name='Quantity')
    total_price = models.FloatField(null=True, blank=True, default=0.0, verbose_name='Total')
    product_status = models.BooleanField(null=True, blank=True, 
                                    verbose_name='In cart')
    category = models.ForeignKey('Category', null=True,
                                 on_delete=models.CASCADE, verbose_name='Category') #on_delete=models.PROTECT - if we want prohib cascade deleting


    @property 
    def total_cost(self): 
        return round((self.quantity * self.price), 2)


    class Meta:
        verbose_name_plural = 'Products'
        verbose_name = 'Product'
        ordering = ['product_status', 'product_name']



class Category(models.Model):
#    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20,
                            verbose_name='Category')

    is_published = models.BooleanField(default=True,
                            verbose_name='Show')

#    products = models.ForeignKey('Products', null=True,  db_index=True,
#                                on_delete=models.CASCADE, verbose_name='Products') )

    def __str__(self): 
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'
        ordering = ['name', 'is_published']