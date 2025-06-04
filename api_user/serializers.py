from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    
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


from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'  # Le dices que use email como username

    def validate(self, attrs):
        # attrs ya tiene 'email' y 'password' como claves, sólo pasas directamente:
        data = super().validate(attrs)
        data['email'] = attrs.get('email')
        return data

