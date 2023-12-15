from django.urls import path
from .views import *

urlpatterns = [
    path('v1/list1/', ProductApiViewset.as_view({'get':'list'}), name='ProductListView'),
    # path('Product/Details/View', ProductDetailView.as_view(), name='ProductDetailsView'),
    # path('v1/create/', ProductApiCreateView.as_view(), name='ProductApiCreateView'),
    path('v1/list/<int:pk>/', ProductApiViewset.as_view({'put':'update'}), name='ProductApiUpdateView'),
    path('v1/list/',CustomProductApiView.as_view(),  name='CustomProductApiView'),
    path('v1/list2/', ProductListAPIView.as_view(), name='CustomProductApiView2'),

]
