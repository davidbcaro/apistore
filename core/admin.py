from django.contrib import admin
from .models import Product, Customer, CustomerProduct, Order, OrderDetail


admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(CustomerProduct)
admin.site.register(Order)
admin.site.register(OrderDetail)
