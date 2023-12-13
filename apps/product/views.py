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

class ProductApiCreateView(generics.CreateAPIView): # создает
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductApiUpdateView(generics.UpdateAPIView): # обновляет
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductApiListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductApiDestroyView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductApiRetrieveView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductApiRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductApiRetrieveDestroyView(generics.RetrieveDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

class ProductApiRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()

