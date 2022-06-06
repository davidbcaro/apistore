from .models import Product, Order, OrderDetail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import ProductSerializer, OrderSerializer, OrderDetailSerializer, OrderListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    #filter_backends = (DjangoFilterBackend,)
    #filter_fields = {'customer': ['exact'], 'creation_date': ['range', 'exact']}


class OrderDetailViewset(viewsets.ModelViewSet):
    queryset = OrderDetail.objects.all()
    serializer_class = OrderDetailSerializer
    

class OrderListView(generics.ListAPIView):
    
    def get_creation_date(self, order):
        return order.creation_date.strftime("%Y-%m-%d")
        #return order.creation_date
    
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = {'customer': ['exact'], 'creation_date': ['range', 'exact']}
    #enderer_classes = (JSONRenderer, BrowsableAPIRenderer)

    
    # def get(self, request):
    #     orders = Order.objects.all()
    #     serializer = OrderListSerializer(orders, many=True)
    #     return Response(serializer.data)
    
    

    