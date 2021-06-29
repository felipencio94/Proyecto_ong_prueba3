from django.shortcuts import render, redirect
from .models import Proveedor
from .forms import ProveedorForm
# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def contacto(request):
    return render(request, 'core/contacto.html') 

def proveedores(request):
    proveedores= Proveedor.objects.all()
    datos = {
        'proveedores' : proveedores
    }
    return render(request,'core/proveedores.html', datos)

def seccion_gatos(request):
    return render(request,'core/seccion-gatos.html')

def seccion_perros(request):
    return render(request,'core/seccion-perros.html')

def form_nuevoProv(request):
    datos = {
        'form': ProveedorForm()
    }
    if request.method== 'POST':
        formulario = ProveedorForm(request.POST)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = 'Proveedor guardado correctamente'
        
    return render(request,'core/form_nuevoProv.html',datos)

def form_modProv(request, id):
    proveedor = Proveedor.objects.get(rut=id)
    datos = {
        'form' : ProveedorForm(instance=proveedor)
    }
    if request.method == 'POST':
        formulario = ProveedorForm(data=request.POST,instance=proveedor)
        if formulario.is_valid:
            formulario.save()
            datos['mensaje'] = "Proveedor modificado correctamente"
    return render(request,'core/form_modProv.html',datos)

def form_delProv(request,id):
    proveedor = Proveedor.objects.get(rut=id)
    proveedor.delete()
    return redirect(to="/proveedores")

