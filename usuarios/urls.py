from django.urls import path
from usuarios.views import login, registro, editar_perfil, CambiarPassword, mostrar_perfil
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/',login, name='login'),
    path('logout/',LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    path('registro/',registro, name='registrarse'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/editar/password/', CambiarPassword.as_view(), name='cambiar_password'),
    path('mostrar_perfil/', mostrar_perfil, name='mostrar_perfil')
    

]
