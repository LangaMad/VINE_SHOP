from django.forms import model_to_dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework.generics import GenericAPIView
from rest_framework.views import APIView
from .models import Product
from rest_framework import generics , mixins
from rest_framework import viewsets
from .serializers import ProductSerializer
from rest_framework.response import Response



class CustomProductApiView(mixins.ListModelMixin,GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# class CustomProductApiView(APIView):
#     def get(self, request):
#         lst = Product.objects.all().values()
#         return  Response(list(lst))
#
#     def post(self, request):
#         post_data = Product.objects.create(
#             name=request.data['name'],
#             description=request.data['description'],
#             price=request.data['price'],
#             count=request.data['count'],
#             public_date=request.data['public_date'],
#             brand = request.data['brand'],
#             photo=request.data['photo'],
# )
#         return Response({'post':model_to_dict(post_data)})
# class ListAPIView(mixins.ListModelMixin,
#                   GenericAPIView):
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)



















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

