# IMPORTS.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    """
    Manager personalizado para el modelo CustomUser.
    Define los métodos para crear usuarios normales y superusuarios.
    """
    def create_user(self, email, rut, password=None, **extra_fields):
        """
        Crea y retorna un usuario con email, rut y demás campos obligatorios.
        """
        if not email:
            raise ValueError('El correo electrónico es obligatorio')
        if not rut:
            raise ValueError('El RUT es obligatorio')
        if not password:
            raise ValueError('La contraseña es obligatoria')
        if not extra_fields.get('nombre'):
            raise ValueError('El nombre es obligatorio')
        if not extra_fields.get('apellido'):
            raise ValueError('El apellido es obligatorio')
        if not extra_fields.get('direccion'):
            raise ValueError('La dirección es obligatoria')
        
        # Valor por defecto para tipo_usuario si no se especifica.
        extra_fields.setdefault('tipo_usuario', 'cliente')

        email = self.normalize_email(email)
        user = self.model(email=email, rut=rut, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, rut, password=None, **extra_fields):
        """
        Crea y retorna un superusuario con permisos de administrador.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('tipo_usuario', 'administrador')

        return self.create_user(email, rut, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Modelo de usuario personalizado que reemplaza al modelo por defecto de Django.
    Utiliza el correo electrónico como identificador principal.
    """
    TIPO_USUARIO_CHOICES = [
        ('cliente', 'Cliente'),
        ('bodeguero', 'Bodeguero'),
        ('vendedor', 'Vendedor'),
        ('administrador', 'Administrador'),
    ]
    
    # Campos personalizados.
    rut = models.CharField(max_length=12, unique=True)
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    direccion = models.TextField()
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES, default='cliente')

    # Campos de control de Django.
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Configuración del modelo.
    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rut', 'nombre', 'apellido', 'direccion']

    def __str__(self):
        """
        Representación legible del usuario.
        """
        return f'{self.email} - {self.rut}'

