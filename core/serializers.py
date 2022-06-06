from rest_framework import serializers
from .models import Customer, CustomerProduct, Product, Order, OrderDetail


class CustomerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Customer
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = '__all__'
        

class CustomerProductSerializer(serializers.ModelSerializer):
    
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = Order
        fields = ('id', 'customer_name', 'product_name')


class OrderDetailSerializer(serializers.HyperlinkedModelSerializer):
    
    customer_name = serializers.CharField(source='order.customer.name', read_only=True)
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = OrderDetail
        fields = ('id', 'order', 'customer_name', 'product', 'product_name', 'quantity')
      

class OrderSerializer(serializers.ModelSerializer):
    
    total = serializers.SerializerMethodField()
    customer_name = serializers.CharField(source='customer.name', read_only=True)
    
    def get_total(self, order):
        order_details = OrderDetail.objects.filter(order=order)
        return sum([order_detail.product.price * order_detail.quantity for order_detail in order_details])
    
    class Meta:
        model = Order
        fields = ('id', 'customer', 'customer_name', 'creation_date', 'delivery_address', 'total')


class OrderListSerializer(serializers.ModelSerializer):
    
    customer = serializers.CharField(source='customer.name')
    total = serializers.SerializerMethodField()
    products = serializers.SerializerMethodField()
    order_details = serializers.CharField(write_only=True)

    def get_total(self, order):
        order_details = OrderDetail.objects.filter(order=order)
        return sum([order_detail.product.price * order_detail.quantity for order_detail in order_details])

    def get_products(self, order):
        order_details = OrderDetail.objects.filter(order=order)
        return ', '.join(["%s x %s" % (order_detail.product.name, order_detail.quantity) for order_detail in order_details])
    
    def create(self, validated_data):
        """
        Create and return a new Order
        """
        order_details = validated_data.get('order_details')
        if len(order_details) > 5:
            raise serializers.ValidationError("Only 5 products are allowed")
        order = Order()
        order.customer = validated_data.get('customer')
        order.delivery_address = validated_data.get('delivery_address')
        order.date = validated_data.get('date')
        order.save()
        for order_detail in order_details:
            order_detail_obj = OrderDetail(**order_detail)
            order_detail_obj.order = order
            order_detail_obj.save()
            if not CustomerProduct.objects.filter(customer=order.customer, product_id=order_detail_obj.product_id).exists():
                order.delete()
                raise serializers.ValidationError(
                    "Product %s is not valid for the user %s" % (order_detail_obj.product, order.customer))
            order_detail_obj.save()
        return order

    def update(self, instance, validated_data):
        """
        Update and return an existing Order
        """
        instance.customer = validated_data.get('customer', instance.customer)
        instance.delivery_address = validated_data.get(
            'delivery_address', instance.delivery_address)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance

    class Meta:
        model = Order
        fields = ('customer', 'creation_date', 'id', 'total', 'delivery_address', 
                  'products', 'order_details')


    