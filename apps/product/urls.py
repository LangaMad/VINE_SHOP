from django.urls import path, include, re_path

from .views import *
from rest_framework.routers import SimpleRouter,DefaultRouter

# router = DefaultRouter()
# router.register('vines', ProductApiViewSet)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/verify/', TokenVerifyView.as_view(), name='token_verify'),
    # path('v1/', include(router.urls)),
    # path('v1/list1/', ProductApiViewset.as_view({'get':'list'}), name='ProductListView'),
    # # path('Product/Details/View', ProductDetailView.as_view(), name='ProductDetailsView'),
    path('v1/list/', ProductApiListCreateView.as_view(), name='ProductApiCreateView'),
    path('v1/delete/', ProductApiDestroyView.as_view(), name='ProductApiDeleteView'),
    # # path('v1/list/<int:pk>/', ProductApiViewset.as_view({'put':'update'}), name='ProductApiUpdateView'),
    # path('v1/list/<int:pk>/',Product2.as_view(),  name='CustomProductApiView'),
    # path('v1/list2/', ProductListAPIView.as_view(), name='CustomProductApiView2'),
    # path('api/v1/auth/', include('djoser.urls')),
    # re_path(r'^auth/', include('djoser.urls.authtoken')),

]
