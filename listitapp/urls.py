from django.urls import path

from . import views #index, create_category, delete_category

urlpatterns = [
    path('', views.index),
    path('listitapp', views.index),    
    path('create_category', views.create_category),
    path('delete_category/<str:pk>', views.delete_category),
    path('shopping_list', views.shopping_list)    
]