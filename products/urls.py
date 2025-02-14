from django.urls import path
from .views import (product_detail_view, product_create_view, 
dynamic_lookup_view,product_delete_view, product_list_view)

app_name= 'products'
urlpatterns = [
    # path('', product_detail_view, name='about'),
    path('<int:my_id>/', dynamic_lookup_view, name='product-detail'),
    path('<int:my_id>/delete/', product_delete_view , name='product_delete'),
    path('', product_list_view, name='product-list'),
]