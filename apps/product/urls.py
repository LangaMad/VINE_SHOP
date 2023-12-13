from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/list',
         ProductListAPIView.as_view(),
         name='ProductListView'),
    path('Product/Details/View',
         ProductDetailView.as_view(),
         name='ProductDetailsView'),
    path('v1/create/',
         ProductApiCreateView.as_view(),
         name='ProductApiCreateView'),
    path('v1/update/<int:pk>/',
         ProductApiUpdateView.as_view(),
         name='ProductApiUpdateView'),
    path('v1/list_create/',
         ProductApiListCreateView.as_view(),
         name='ProductListCreateView'),
    path('v1/destroy/<int:pk>/',
         ProductApiDestroyView.as_view(),
         name='ProductApiDestroyView'),
    path('v1/retrieve/<int:pk>/',
         ProductApiRetrieveView.as_view(),
         name='ProductApiRetrieveView'),
    path('v1/retrieve_update/<int:pk>/',
         ProductApiRetrieveUpdateView.as_view(),
         name='ProductApiRetrieveUpdateView'),
    path('v1/retrieve_destroy/<int:pk>/',
         ProductApiRetrieveDestroyView.as_view(),
         name='ProductApiRetrieveDestroyView'),
    path('v1/retrieve_update_destroy/<int:pk>/',
         ProductApiRetrieveUpdateDestroyView.as_view(),
         name='ProductApiRetrieveUpdateDestroyView'),
]



