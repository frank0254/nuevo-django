from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from django.template import loader 
from inicio.models import Autos, Motos, Bicicletas
from inicio.forms import CrearAutoFormulario
from inicio.forms import CrearMotoFormulario
from inicio.forms import CrearBicicletaFormulario
# Create your views here.

def inicio(request):
#version 2    
    #template = loader.get_template('inicio.html')
    #template_renderizado = template.render({})
    
    #return HttpResponse(template_renderizado)
    
#ultima version mejorada v3
    return render(request,'inicio/inicio.html', {})

def auto(request):
    
#para crear formulario de busqueda
    marca_a_buscar = request.GET.get("marca")
    if marca_a_buscar:
        listado_de_auto = Autos.objects.filter(marca__icontains =marca_a_buscar.lower())
    else:
        listado_de_auto = Autos.objects.all()
    return render(request, 'inicio/vehiculo.html', {'listado_de_auto': listado_de_auto})    
    
    listado_de_auto = Autos.objects.all()
   
    #return render(request, 'inicio/vehiculo.html', {'listado_de_auto': listado_de_auto})

def moto(request):
    
    listado_de_moto = Motos.objects.all()
   
    return render(request, 'inicio/vehiculo.html', {'listado_de_moto': listado_de_moto})

def bicicletas(request):
    
    listado_de_bicicleta = Bicicletas.objects.all()
   
    return render(request, 'inicio/vehiculo.html', {'listado_de_moto': listado_de_bicicleta})
    
    
def crear_auto(request):
    
        
    if request.method == 'POST':
        formulario = CrearAutoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
    
            auto = Autos(marca=marca, descripcion=descripcion, anio=anio)    
            auto.save()
            
            return redirect(crear_auto)
        else:
            return render(request, 'inicio/auto.html', {'formulario': formulario})
        
    formulario = CrearAutoFormulario()
    return render(request, 'inicio/auto.html', {'formulario': formulario})


def crear_moto(request):
        
    if request.method == 'POST':
        formulario = CrearMotoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            modelo = info_limpia.get('modelo')
            precio = info_limpia.get('precio')
    
            moto = Motos(marca=marca, descripcion=descripcion, anio=anio, modelo=modelo, precio=precio)    
            moto.save()
            
            return redirect(crear_auto)
        else:
            return render(request, 'inicio/moto.html', {'formulario': formulario})
        
    formulario = CrearMotoFormulario()
    return render(request, 'inicio/moto.html', {'formulario': formulario})

def crear_bicicleta(request):
        
    if request.method == 'POST':
        formulario = CrearBicicletaFormulario(request.POST)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
    
            bicicleta = Bicicletas(marca=marca, descripcion=descripcion, anio=anio)    
            bicicleta.save()
            
            return redirect(crear_auto)
        else:
            return render(request, 'inicio/bicicleta.html', {'formulario': formulario})
        
    formulario = CrearBicicletaFormulario()
    return render(request, 'inicio/bicicleta.html', {'formulario': formulario})