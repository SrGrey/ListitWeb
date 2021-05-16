from django.urls import path

from . import views #index, create_category, delete_category

urlpatterns = [
    path('', views.index),
    path('listitapp', views.index),    
    path('create_category', views.create_category),
    path('delete_category/<str:pk>', views.delete_category),
    path('hide_category/<str:pk>', views.hide_category),
    path('delete_product/<str:pk>', views.delete_product),
    path('create_product/<str:pk>', views.create_product),
    path('shopping_list', views.shopping_list)    
]
