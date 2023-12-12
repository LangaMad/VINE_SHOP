from django.urls import path
from .views import *

urlpatterns = [
    path('api/v1/list', UserAPIListVIew.as_view(), name='UserListView'),
]
