# IMPORTS.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer

# ============================================
#               VISTAS HTML
# ============================================
# Vista de signup, crear usuario, vista HTML.
def signup_view(request):
    return render(request, 'api_user/signup.html')

# Vista de login, iniciar sesión, vista HTML.
def login_view(request):
    return render(request, 'api_user/login.html')

# ============================================
#               VISTAS API
# ============================================
# Metodo POST.
# Endpoint API para registrar un nuevo usuario.
@api_view(['POST'])
def signup_api(request):
    serializer = CustomUserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Usuario creado correctamente'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Metodo GET.
# Endpoint API para listar todos los usuarios registrados.
@api_view(['GET'])
def list_users_api(request):
    users = CustomUser.objects.all()
    serializer = CustomUserSerializer(users, many=True)
    return Response(serializer.data)

# Metodo personalizado para la autentificación.
class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer