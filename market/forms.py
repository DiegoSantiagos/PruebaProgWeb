from django import forms
from django.forms import ModelForm
from .models import Usuario, Productos, Categoria

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'foto', 'email', 'contrasena']
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
        
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripcion'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre de la categoria'
                }),

            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la descripcion de la categoria'
                })
        }
    