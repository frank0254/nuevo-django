from django.shortcuts import render, redirect
#from django.http import HttpResponse
#from django.template import loader 
from inicio.models import Autos, Motos, Bicicletas
from inicio.forms import CrearAutoFormulario
from inicio.forms import CrearMotoFormulario
from inicio.forms import CrearBicicletaFormulario
from inicio.forms import ModificarAutoFormulario
from django.contrib.auth.decorators import login_required



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
        
    if not listado_de_auto:
        mensaje = 'no se encontraron datos buscados'
    else:
        mensaje = ''
    return render(request, 'inicio/vehiculo.html', {'listado_de_auto': listado_de_auto, 'mensaje':mensaje})    
    
    listado_de_auto = Autos.objects.all()
   
    #return render(request, 'inicio/vehiculo.html', {'listado_de_auto': listado_de_auto})

def moto(request):
    
    listado_de_moto = Motos.objects.all()
   
    return render(request, 'inicio/vehiculo.html', {'listado_de_moto': listado_de_moto})

def bicicletas(request):
    
    listado_de_bicicleta = Bicicletas.objects.all()
   
    return render(request, 'inicio/vehiculo.html', {'listado_de_moto': listado_de_bicicleta})
    
@login_required    
def crear_auto(request):
    
    if request.method == 'POST':
        formulario = CrearAutoFormulario(request.POST, request.FILES)
        if formulario.is_valid():
            info_limpia = formulario.cleaned_data
            
            marca = info_limpia.get('marca')
            descripcion = info_limpia.get('descripcion')
            anio = info_limpia.get('anio')
            modelo = info_limpia.get('modelo')
            imagen_a_agregar = info_limpia.get('imagen_a_agregar') 
            fecha_de_creacion = info_limpia.get('fecha_de_creacion')
    
            auto = Autos(marca=marca, descripcion=descripcion, anio=anio, modelo=modelo, imagen_a_agregar=imagen_a_agregar, fecha_de_creacion=fecha_de_creacion)    
            auto.save()
            
            return redirect(crear_auto) 
        else:
            return render(request, 'inicio/auto.html', {'formulario': formulario})
        
    formulario = CrearAutoFormulario()
    return render(request, 'inicio/auto.html', {'formulario': formulario})

@login_required 
def eliminar_auto(request, auto_id):
    auto_a_eliminar= Autos.objects.get(id=auto_id)
    auto_a_eliminar.delete()    
    return redirect("auto")

@login_required 
def modificar_auto(request, auto_id):
    auto_a_modificar = Autos.objects.get(id=auto_id)
    
    if request. method == "POST":
        formulario = ModificarAutoFormulario(request.POST)
        if formulario.is_valid():
            info_nueva = formulario.cleaned_data
            
            auto_a_modificar.marca = info_nueva.get('marca')
            auto_a_modificar.descripcion = info_nueva.get('descripcion')
            auto_a_modificar.anio = info_nueva.get('anio')
            auto_a_modificar.modelo = info_nueva.get('modelo')
            auto_a_modificar.imagen_a_agregar = info_nueva.get('imagen_a_agregar')
            auto_a_modificar.fecha_de_creacion = info_nueva.get('fecha_de_creacion')
            
            auto_a_modificar.save()
            return redirect('auto')
        return render(request, 'inicio/modificar_auto.html', {'formulario': formulario})
    
    formulario = ModificarAutoFormulario(initial={'marca': auto_a_modificar.marca, 'anio':auto_a_modificar.anio, 'descripcion': auto_a_modificar.descripcion, 'modelo': auto_a_modificar.modelo, 'imagen_a_agregar': auto_a_modificar.imagen_a_agregar, 'fecha_de_creacion': auto_a_modificar.fecha_de_creacion} )
    return render(request, "inicio/modificar_auto.html", {'formulario': formulario})
    
def detalle_auto(request, auto_id):
    auto = Autos.objects.get(id=auto_id)
    

    return render(request, 'inicio/detalle_auto.html', {'auto': auto})





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

