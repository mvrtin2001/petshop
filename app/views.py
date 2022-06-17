from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from .froms import ContactoForm, ProductoForm
# Create your views here.


def home(request):
    productos = Producto.objects.all()
    data = {
        'productos': productos
    }
    return render(request, 'app/home.html', data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }
    
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "contacto guardado"
        else: 
            data["form"] = formulario
            
    return render(request, 'app/contacto.html', data)

def galeria(request):
    return render(request, 'app/galeria.html')

def añadir_producto(request):
    data = {
        'form': ProductoForm()
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Añadido Correctamente"
        else:
            data["form"] = formulario
        
    return render(request, 'app/producto/añadir.html', data)


def agrupar_productos(request):
    productos = Producto.objects.all()
    
    data = {
        'productos': productos
    }
    return render(request, 'app/producto/agrupar.html', data)

def editar_producto(request, id):
    
    producto = get_object_or_404(Producto, id=id)
    
    data= {
        'form': ProductoForm(instance=producto)
    }
    
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="agrupar_productos")
        data["form"] = formulario
    
    return render(request, 'app/producto/editar.html', data)

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect(to="agrupar_productos")