from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewset, OrderViewset, OrderDetailViewset, OrderListView, CustomerViewset, CustomerProductViewset

router = DefaultRouter()
router.register('customer', CustomerViewset)
router.register('product', ProductViewset)
router.register('customerproduct', CustomerProductViewset)
router.register('order', OrderViewset)
router.register('orderdetail', OrderDetailViewset)

urlpatterns = [
    path('', include(router.urls)),
    path('orderlist/', OrderListView.as_view(), name='orderlist'),
]