# urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('cart/<str:action>/<int:item_id>/', CartActionView.as_view(), name='CartActionView'),
]
