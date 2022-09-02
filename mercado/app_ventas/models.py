from django.db import models
from datetime import datetime


class categoria(models.Model):
    nombre_categoria = models.CharField(max_length=160, verbose_name='Categoria')

    def __str__(self):
        return self.nombre_categoria

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']

class producto(models.Model):
    nombre_producto = models.CharField(max_length=160, verbose_name='Producto')
    categoria_prodcut = models.ForeignKey(categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='producto%Y/%m/%d', null=True, blank=True)
    precio_prducto = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    
    def __str__(self):

        return self.nombre_producto

    class Meta:
        verbose_name = 'Prodcuto'
        verbose_name_plural = 'Productos'
        ordering = ['id']

class cliente(models.Model):
    nombre_cliente = models.CharField(max_length=150, verbose_name='Nombre cliente')
    apellido_cliente = models.CharField(max_length=150, verbose_name='Apellido cliente')
    dpi = models.CharField(max_length=15, verbose_name='Documento Personal de Identificacion')
    fecha_nac = models.DateField(default=datetime.now, verbose_name='fecha nacimiento')
    direccion = models.CharField(max_length=200, null=True, blank=True, verbose_name='Direccion domiciliar')
    models.CharField(max_length=10,  verbose_name='Sexo')

    def __str__(self):

        return self.nombre_cliente

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['id']


class venta(models.Model):
    cliente_venta = models.ForeignKey(cliente, on_delete=models.CASCADE)
    fecha_registro = models.DateField(default=datetime.now)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):

        return str(self.cliente_venta)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['id']

class detalle_venta(models.Model):
    detalle_venta = models.ForeignKey(venta, on_delete=models.CASCADE)
    detalle_producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    precio = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    cantidad = models.IntegerField(default=0,)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):

        return self.nombre_producto

    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalle Ventas'
        ordering = ['id']