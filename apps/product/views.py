from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product
# Create your views here.
class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product_detail'
    queryset = Product.objects.all()