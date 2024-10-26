from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    direccionUsuario = models.CharField(max_length=100)
    telefonoUsuario = models.CharField(max_length=25)

    def __str__(self):
        return self.user.username
    