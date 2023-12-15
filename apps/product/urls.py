from django.urls import path
from .views import *

urlpatterns = [
    # path('v1/list/<int:pk>', ProductListAPIView.as_view(), name='ProductListView'),
    path('Product/Details/View', ProductDetailView.as_view(), name='ProductDetailsView'),
    path('v1/create/', ProductApiCreateView.as_view(), name='ProductApiCreateView'),
    path('v1/update/<int:pk>', ProductApiUpdateView.as_view(), name='ProductApiUpdateView'),
    path('v1/retrive/<int:pk>', ProductApiRetriveUpdateDestroyView.as_view(), name='ProductApiUpdateView'),
    path('v1/list',ProductApiViewset.as_view({"put":'list'}), name='ProductApiViewset'),
    path('v1/list/<int:pk>',ProductApiViewset.as_view({"put":'update'}), name='ProductApiViewset')
]