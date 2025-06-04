from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.models import Group
from django.contrib.auth.admin import AdminPasswordChangeForm
from django.utils.translation import gettext_lazy as _
from django import forms

class CustomUserCreationForm(forms.ModelForm):
    """Formulario para crear usuarios en el admin."""
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('rut', 'email', 'nombre', 'apellido', 'direccion')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

class CustomUserChangeForm(forms.ModelForm):
    """Formulario para editar usuarios en el admin."""
    class Meta:
        model = CustomUser
        fields = ('rut', 'email', 'nombre', 'apellido', 'direccion', 'is_active', 'is_staff', 'is_superuser')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('rut', 'email', 'nombre', 'apellido', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    fieldsets = (
        (None, {'fields': ('rut', 'email', 'password')}),
        ('Información Personal', {'fields': ('nombre', 'apellido', 'direccion')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('rut', 'email', 'nombre', 'apellido', 'direccion', 'password', 'is_staff', 'is_superuser')}
        ),
    )
    search_fields = ('rut', 'email', 'nombre', 'apellido')
    ordering = ('email',)
