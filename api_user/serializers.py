# IMPORTS.
from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

# ===============================================
#         SERIALIZER PARA REGISTRO DE USUARIOS
# ===============================================
class CustomUserSerializer(serializers.ModelSerializer):
    """
    Serializer para crear y representar instancias del modelo CustomUser.
    Utilizado principalmente en el endpoint /api/signup/ para registrar nuevos usuarios.
    """
    class Meta:
        model = CustomUser
        fields = ['rut', 'email', 'password', 'nombre', 'apellido', 'direccion']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            rut=validated_data['rut'],
            email=validated_data['email'],
            password=validated_data['password'],
            nombre=validated_data['nombre'],
            apellido=validated_data['apellido'],
            direccion=validated_data['direccion']
        )
        return user

# ===============================================
#        SERIALIZER PERSONALIZADO PARA JWT
# ===============================================

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """
    Serializer personalizado para la autenticación JWT.
    Permite iniciar sesión usando el campo 'email' en lugar de 'username'.

    Se utiliza en CustomLoginView para emitir access y refresh tokens.
    """
    username_field = 'email'

    def validate(self, attrs):
        data = super().validate(attrs)
        data['email'] = attrs.get('email')
        return data

