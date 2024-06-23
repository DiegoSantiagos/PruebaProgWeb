from django import forms
from django.forms import ModelForm
from .models import Usuario, Productos

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'foto', 'email', 'telefono', 'contrasena']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'foto': 'Foto de perfil',
            'email': 'email',
            'telefono': 'Telefono',
            'contrasena': 'Contrasena'
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
            'foto': forms.FileInput(attrs={
                'class': 'form-control'
                }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su email'
                }),

            'telefono': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su telefono'
                }),

            'contrasena': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese contraseña'
                })
        }
    
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'precio', 'imagen', 'descripcion', 'Categoria']
        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'imagen': 'Imagen',
            'descripcion': 'Descripcion',
            'Categoria': 'Categoria'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del producto'
                }),

            'precio': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el precio del producto'
                }),

            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control'
                }),

            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la descripcion del producto'
                }),

            'Categoria': forms.Select(attrs={
                'class': 'form-control'
                }) 
        }
    