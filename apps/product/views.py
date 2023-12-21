from django.forms import model_to_dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework.generics import GenericAPIView

from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from .models import Product, Category
from rest_framework import generics , mixins
from rest_framework import viewsets
from .serializers import ProductSerializer
from rest_framework.response import Response

from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, AllowAny

# Метод Get используется для получения данных
# Метод Post используется для отправки данных
# Метод Put используется для обновления данных
# Метод Patch используется для обновления какой-либо части данных
# Метод Delete используется для удаления данных
# Метод Head используется для проверки существования данных
# Метод Options используется для получения списка доступных методов

class ProductApiListCreateView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)


class ProductApiDestroyView(generics.ListAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)

class ProductApiUpdateView(generics.UpdateAPIView): # Обновляет обьект
    serializer_class = ProductSerializer
    queryset = Product.objects.all()









#
# class ProductApiViewSet(mixins.CreateModelMixin,
#                    mixins.RetrieveModelMixin,
#                    mixins.UpdateModelMixin,
#                    mixins.DestroyModelMixin,
#                    mixins.ListModelMixin,
#                    GenericViewSet):
#     serializer_class = ProductSerializer
#     queryset = Product.objects.all()
#     @action(methods=['get'], detail=True)
#     def category(self, request,pk=None):
#         cats = Category.objects.get(id=pk)
#         return Response({'cats':cats.title})

#
# class CustomProductApiView(mixins.ListModelMixin,
#                            mixins.RetrieveModelMixin,
#                            mixins.CreateModelMixin,
#                            mixins.DestroyModelMixin,
#                            GenericAPIView):
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
#
# class Product2(generics.CustomProductApiView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


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






















class ProductApiCreateView(generics.CreateAPIView): # Создает обьект
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

