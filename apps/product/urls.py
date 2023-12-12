from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/list', ProductListAPIView.as_view(), name='ProductListView'),
    path('Product/Details/View', ProductDetailView.as_view(), name='ProductDetailsView')
]