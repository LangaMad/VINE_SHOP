from django.urls import path
from .views import *

urlpatterns = [
    path('v1/list/', ProductApiViewset.as_view({'get':'list'}), name='ProductListView'),
    # path('Product/Details/View', ProductDetailView.as_view(), name='ProductDetailsView'),
    # path('v1/create/', ProductApiCreateView.as_view(), name='ProductApiCreateView'),
    path('v1/list/<int:pk>/', ProductApiViewset.as_view({'put':'update'}), name='ProductApiUpdateView'),

]