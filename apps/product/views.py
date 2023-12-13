from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from rest_framework import generics
from rest_framework import views
from .serializers import ProductSerializer
# Create your views here.
class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    context_object_name = 'products'
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product_detail'
    queryset = Product.objects.all()
