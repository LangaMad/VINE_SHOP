from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
from rest_framework import generics, viewsets
from .serializers import ProductSerializer

class ProductApiViewset(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


# Create your views here.
class ProductListAPIView(generics.ListAPIView):
    serializer_class = ProductSerializer
    context_object_name = 'products'
    queryset = Product.objects.all()

class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product_detail'
    queryset = Product.objects.all()

class ProductApiCreateView(generics.CreateAPIView):
    serializer_class = ProductSerializer
    model = Product
    context_object_name = 'product_detail'
    queryset = Product.objects.all()


class ProductApiUpdateView(generics.UpdateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductApiRetriveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()