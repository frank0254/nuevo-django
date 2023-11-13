from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm    
from django.contrib.auth import authenticate, login as django_login
from usuarios.forms import MiFormularioDeCreacion,  EdicionPerfilFormulario
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from usuarios.models import Datos



# Create your views here.
def login(request):
    
    formulario = AuthenticationForm()
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contra =  formulario.cleaned_data.get('password') 
            
            user = authenticate(username=usuario, password=contra)   
            
            django_login(request,user)
            
            Datos.objects.get_or_create(user= request.user)
            return redirect('inicio')     
       
    return render(request, 'usuarios/login.html', {'formulario_de_login': formulario})      
            

def registro(request):
    formulario = MiFormularioDeCreacion()
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            
            formulario.save()
            
            return redirect('login')
 
    return render(request, 'usuarios/registro.html', {'formulario_de_registro': formulario})         

def editar_perfil(request):
    datos = request.user.datos
    
    formulario = EdicionPerfilFormulario(initial={'biografia': datos.biografia, 'avatar':datos.avatar})
    
    if request.method == 'POST':
        formulario = EdicionPerfilFormulario(request.POST, request.FILES, instance= request.user)
        
        if formulario.is_valid():
            
            nueva_biografia= formulario.cleaned_data.get('biografia')
            nueva_avatar= formulario.cleaned_data.get('avatar')
           
            if nueva_biografia:
                datos.biografia = nueva_biografia
            if  nueva_avatar:
                datos.avatar =nueva_avatar
            
            datos.save()
            formulario.save()
            return redirect('editar_perfil')

    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})
            

class CambiarPassword(PasswordChangeView):
    template_name = 'usuarios/cambiar_password.html'
    success_url = reverse_lazy('editar_perfil')
    
    
    
def mostrar_perfil(request):
    datos = request.user.datos
    return render(request, 'usuarios/mostrar_perfil.html', {'datos': datos})
    
    