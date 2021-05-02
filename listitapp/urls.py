from django.urls import path

from .views import index, create_category

urlpatterns = [
    path('', index),
    path('create_category', create_category),
]