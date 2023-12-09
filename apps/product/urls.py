from django.urls import path
from .views import *

urlpatterns = [
    path('product/list/', ProductListView.as_view(), name='product_list'),
    path('product/detail/', ProductDetailView.as_view(), name='product_detail'),
]
