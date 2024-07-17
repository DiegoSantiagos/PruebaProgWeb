from django import forms
from django.forms import ModelForm
from .models import Usuario, Productos, Categoria, Direccion, MetodoPago
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
    
class DireccionForm(forms.ModelForm):
    class Meta:
        model = Direccion
        fields = ['direccion', 'ciudad', 'estado', 'pais', 'codigo_postal']
        labels = {
            'direccion': 'Direccion',
            'ciudad': 'Ciudad',
            'estado': 'Estado',
            'pais': 'Pais',
            'codigo_postal': 'Codigo postal'
        }
        widgets = {
            'direccion': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su direccion'
                }),

            'ciudad': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su ciudad'
                }),

            'estado': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su estado'
                }),

            'pais': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese su pais'
                }),

            'codigo_postal': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'codigo_postal',
                'min': '0',
                'max': '9999999999',
                'placeholder': 'Ingrese su codigo postal'
                })
        }
        
class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = ['nombre', 'numero', 'mesExpiracion', 'anioExpiracion', 'cvv']
        labels = {
            'nombre': 'Nombre',
            'numero': 'Numero',
            'mesExpiracion': 'Fecha de expiracion',
            'anioExpiracion': '',
            'cvv': 'CVV'
        }
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el nombre'
                }),

            'numero': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'numero',
                'min': '0',
                'max': '9999999999999999',
                'placeholder': 'Ingrese el numero de la tarjeta'
                }),
            
            'mesExpiracion': forms.Select(choices=[(i, i) for i in range(1, 13)], attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el mes de expiracion'
            }),
            'anioExpiracion': forms.Select(choices=[(i, i) for i in range(24, 40)], attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese el mes de expiracion'
            }),
            'cvv': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'cvv',
                'min': '100',
                'max': '999',
                'placeholder': 'CVV'
                })
        }