# IMPORTS.
from django.urls import path
# Desde views.py se importan las siguientes vistas.
from .views import signup_view, login_view, signup_api, list_users_api, CustomLoginView

urlpatterns = [
# ============================================
#               VISTAS HTML
# ============================================
    # Vista de signup, crear usuario, vista HTML.
    path('signup/', signup_view, name='signup'),
    # Vista de login, iniciar sesión, vista HTML.
    path('login/', login_view, name='login'),
    
# ============================================
#               VISTAS API
# ============================================
    # Vista de signup, crear usuario, vista EndPoint.
    path('api/signup/', signup_api, name='api_signup'),
    # Vista de login, iniciar sesión, vista EndPoint.
    path('api/login/', CustomLoginView.as_view(), name='api-login'),
    # Vista que lista los usuarios, vista EndPoint.
    path('api/users/', list_users_api, name='list_users_api'),
]
