from django.shortcuts import render

# Create your views here.

def index(request):
    context = {}
    return render(request, 'market/index.html', context)

def listarProductos(request):
    context = {}
    return render(request, 'market/listarProductos.html', context)
