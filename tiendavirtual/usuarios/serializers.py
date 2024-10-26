from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
        
        
class RegistroUsuarioSerializer(serializers.ModelSerializer):
    direccionUsuario = serializers.CharField(source='perfil.direccionUsuario')
    telefonoUsuario = serializers.CharField(source='perfil.telefonoUsuario')

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'direccionUsuario', 'telefonoUsuario']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        perfil_data = validated_data.pop('perfil')
        
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
            
        )
        
        Usuario.objects.update_or_create(
            user=user,
            defaults={
                'direccionUsuario': perfil_data['direccionUsuario'],
                'telefonoUsuario': perfil_data['telefonoUsuario']
            }

        )
        return user
