from django.db import models


class Product(models.Model):
    """ 
    Model used to represent a product 
    """
    name = models.CharField(max_length=191, blank=False, null=False, verbose_name='Nombre producto')
    description = models.TextField(blank=False, null=False, verbose_name='Descripción')
    price = models.FloatField(blank=False, null=False, verbose_name='Precio')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['id']


class Customer(models.Model):
    """ 
    Model used to represent a customer 
    """
    name = models.CharField(max_length=191, blank=False, null=False, verbose_name='Nombre cliente')
    email = models.EmailField(blank=False, null=False, verbose_name='Correo electrónico')
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'cliente'
        ordering = ['id']
        

class CustomerProduct(models.Model):
    """ 
    Model used to represent a available product 
    """
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, verbose_name='Cliente')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='Producto')

    def __str__(self):
        return f'{self.customer.name} - {self.product.name}'
    
    class Meta:
        verbose_name = 'Producto disponible'
        verbose_name_plural = 'Productos disponibles'
        db_table = 'producto_disponible'
        ordering = ['id']
        
        
class Order(models.Model):
    """ 
    Model used to represent a order 
    """
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, verbose_name='Cliente')
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    delivery_address = models.CharField(max_length=191, blank=False, null=False, verbose_name='Dirección de entrega')
    
    def __str__(self):
        return self.customer.name
    
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        db_table = 'pedido'
        ordering = ['id']
        
        
class OrderDetail(models.Model):
    """ 
    Model used to represent a order detail 
    """
    order = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Pedido')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
    quantity = models.IntegerField(blank=False, null=False, verbose_name='Cantidad')
    
    def __str__(self):
        return f'{self.order.customer.name} - {self.product.name} ( x {self.quantity} )'
    
    class Meta:
        verbose_name = 'Detalle del pedido'
        verbose_name_plural = 'Detalles del pedido'
        db_table = 'detalle_pedido'
        ordering = ['id']
        


    
