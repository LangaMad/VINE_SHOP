from django.urls import path
from .views import *

urlpattern = [
    path('Produtc/List/View', ProductListView.as_view(), name='ProductListView'),
    path('Product/Details/View', ProductDetailView.as_view(), name='ProductDetailsView')
]