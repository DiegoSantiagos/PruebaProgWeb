from django.urls import path
from . import views

urlpatterns = [
    path('', views.menu, name='menu'),
    path('index', views.index, name='index'),
    path('listarProductos', views.listarProductos, name='listarProductos'),
]