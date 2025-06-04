from django.urls import path
from . import views
from .views import signup_api, list_users_api, CustomLoginView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('api/signup/', signup_api, name='api_signup'),
    path('api/users/', list_users_api, name='list_users_api'),
    path('api/login/', CustomLoginView.as_view(), name='api-login'),
]
