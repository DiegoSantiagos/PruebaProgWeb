from django import forms
from django.forms import ModelForm
from .models import Usuario, Productos

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'correo', 'telefono', 'direccion', 'contrasena', 'foto']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'correo': 'Correo',
            'telefono': 'Telefono',
            'direccion': 'Direccion',
            'contrasena': 'Contrasena',
            'foto': 'Foto de perfil'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su nombre'
                }),

            'apellido': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su apellido'
                
                }),

            'correo': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su correo'
                }),

            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su telefono'
                }),

            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su residencia'
                }),

            'contrasena': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese contraseña'
                }),
            'foto': forms.FileInput(attrs={
                'class': 'form-control'
                })
        }
    
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'descripcion', 'imagen']