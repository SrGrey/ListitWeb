from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('listitapp', views.index),
    path('create_category', views.create_category),
    path('delete_category/<str:pk>', views.delete_category),
    path('hide_category/<str:pk>', views.hide_category),
    path('show_category/<str:pk>', views.show_category),
    path('hide_product/<str:pk>', views.hide_product),
    path('show_product/<str:pk>', views.show_product),
    path('delete_product/<str:pk>', views.delete_product),
    path('create_product/<str:pk>', views.create_product),
    path('modify_product/<str:pk>', views.modify_product),
    path('modify_product_status/<str:pk>', views.modify_product_status,  name='modify_product_status'),# ajax
    path('shopping_list', views.shopping_list),
    path('actual_list', views.actual_list),
    path('add_default_categories', views.add_default_categories),
    path('login', views.login_form),
    path('calculate_total/<str:pk>', views.calculate_total, name='calculate_total'),# ajax
]
