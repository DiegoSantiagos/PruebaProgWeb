from django import forms
from django.forms import ModelForm
from .models import Usuario, Productos, Categoria
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class CustomUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username' , 'password1' , 'password2']

class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'apellido', 'foto', 'email', 'contrasena']
        labels = {
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'foto': 'Foto de perfil',
            'email': 'email',
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
        fields = ['nombre', 'precio', 'imagen', 'descripcion', 'stock', 'Categoria']
        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
            'imagen': 'Imagen',
            'descripcion': 'Descripcion',
            'sock': 'Stock',
            'Categoria': 'Categoria'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre del producto'
                }),

            'precio': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el precio del producto',
                'min': '0'
                
                }),

            'imagen': forms.ClearableFileInput(attrs={
                'class': 'form-control'
                }),

            'descripcion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la descripcion del producto'
                }),
            
            'stock': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese la cantidad de stock del producto',
                'min': '0'
                }),

            'Categoria': forms.Select(attrs={
                'class': 'form-control'
                }) 
        }
    def clean_precio(self):
        precio = self.cleaned_data.get('precio')
        if precio is not None and precio < '0':
            raise ValidationError('El precio no puede ser negativo.')
        return precio

    def clean_stock(self):
        stock = self.cleaned_data.get('stock')
        if stock is not None and stock < 0:
            raise ValidationError('El stock no puede ser negativo.')
        return stock
    
        
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
    