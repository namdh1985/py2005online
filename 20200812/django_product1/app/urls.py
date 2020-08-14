from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('create_category', createCategory),
    path('update_category/<pk>', updateCategory), 
    path('delete_category/<pk>', deleteCategory), 

    path('list_product', listProduct),
    path('create_product', createProduct),
    path('update_product/<pk>', updateProduct), 
    path('delete_product/<pk>', deleteProduct),
]