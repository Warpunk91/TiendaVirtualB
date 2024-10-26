from django.db import models
from tiendas.models import Tienda


class Producto(models.Model):
    idTienda = models.ForeignKey(Tienda, on_delete=models.CASCADE, related_name="productos")
    nombreProducto = models.CharField(max_length=100)
    descripcionProducto = models.CharField(max_length=255)
    tipoProducto = models.CharField(max_length=25)
    precioProducto = models.DecimalField(max_digits=12, decimal_places=2)
    imagenUrlProducto = models.CharField(max_length=255)
    estadoProducto = models.BooleanField()

    def __str__(self):
        return self.nombreProducto