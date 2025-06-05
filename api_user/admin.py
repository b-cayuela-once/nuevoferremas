# IMPORTS.
from django.contrib import admin
from .models import CustomUser
from django import forms

# --------------------------------------
# Formulario personalizado para crear usuarios.
# --------------------------------------
class CustomUserCreationForm(forms.ModelForm):
    """
    Formulario usado para crear usuarios desde el panel de administración.
    Requiere establecer manualmente la contraseña.
    """
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


# --------------------------------------
# Formulario personalizado para editar usuarios.
# --------------------------------------
class CustomUserChangeForm(forms.ModelForm):
    """
    Formulario usado para editar usuarios existentes desde el panel de administración.
    """
    class Meta:
        model = CustomUser
        fields = ('rut', 'email', 'nombre', 'apellido', 'direccion', 'is_active', 'is_staff', 'is_superuser')


# --------------------------------------
# Configuración del panel de administración para CustomUser.
# --------------------------------------
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    """
    Clase que configura la forma en que el modelo CustomUser se muestra en el panel de administración.
    """
    add_form = CustomUserCreationForm # Formulario al crear.
    form = CustomUserChangeForm       # Formulario al editar.
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
