from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader 
from inicio.models import Autos, Motos, Bicicletas

# Create your views here.

def inicio(request):
#version 2    
    #template = loader.get_template('inicio.html')
    #template_renderizado = template.render({})
    
    #return HttpResponse(template_renderizado)
    
#ultima version mejorada v3
    return render(request,'inicio/inicio.html', {})

def crear_auto(request):
    
    auto = Autos(marca= 'wilson', descripcion= 'corsa', anio=2022)    
    auto.save()
    return render(request, 'inicio/vehiculo.html', {'vehiculo':auto, "mensaje": "el Auto"})

def crear_moto(request):
    
    moto = Motos(marca= 'honda', descripcion= 'corsa', anio=2022)    
    moto.save()
    return render(request, 'inicio/vehiculo.html', {'vehiculo': moto, "mensaje": "la Moto"})

def crear_bicicletas(request):
    
    bicicletas = Bicicletas(marca= 'bmx', descripcion= 'corsa', anio=2022)    
    bicicletas.save()
    return render(request, 'inicio/vehiculo.html', {'vehiculo': bicicletas,"mensaje": "la bicicletas"})
    
    