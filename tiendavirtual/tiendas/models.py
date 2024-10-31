from django.db import models
from django.contrib.auth.models import User

class Tienda(models.Model):
    nombreTienda = models.CharField(max_length=100)
    descripcionTienda = models.CharField(max_length=255)
    direccionTienda = models.CharField(max_length=100)
    telefonoTienda = models.CharField(max_length=25)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    UrlImgTienda = models.ImageField(upload_to='imagenes/')
    estadoTienda = models.BooleanField()

    def __str__(self):
        return self.nombreTienda
