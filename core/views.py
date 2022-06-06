from .models import Customer, Product, Order, OrderDetail, CustomerProduct
from rest_framework import viewsets
from .serializers import ProductSerializer, OrderSerializer, OrderDetailSerializer, OrderListSerializer, CustomerSerializer, CustomerProductSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class CustomerProductViewset(viewsets.ModelViewSet):
    queryset = CustomerProduct.objects.all()
    serializer_class = CustomerProductSerializer


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailViewset(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    

class OrderListView(generics.ListAPIView):
    
    def get_creation_date(self, order):
        return order.creation_date.strftime("%Y-%m-%d")
    
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'customer': ['exact'], 'creation_date': ['range', 'exact']}

    
    

    