from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from rest_framework import generics
from rest_framework import viewsets
from .serializers import ProductSerializer
# Create your views here.

class ProductApiViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    context_object_name = 'products'
    queryset = Product.objects.all()

class ProductApiCreateView(generics.CreateAPIView): # Создает обьект
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductApiUpdateView(generics.UpdateAPIView): # Обновляет обьект
    serializer_class = ProductSerializer
    queryset = Product.objects.all()








class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product_detail'
    queryset = Product.objects.all()
