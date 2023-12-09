from django.urls import path
from .views import *

urlpattern = [
    path('ProdutcListView', ProductListView.as_view(), name='ProductListView'),
    path ('ProductDetailsView', ProductDetailView.as_view(), name='ProductDetailsView')
]