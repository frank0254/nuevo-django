from django.urls import path
from inicio.views import inicio, auto, moto, bicicletas, crear_auto, crear_moto, crear_bicicleta

urlpatterns = [
    path('', inicio, name='inicio'),
    path('auto/',auto,name='auto'), 
    path('moto/',moto,name='moto'),
    path('bicicletas/',bicicletas,name='biciletas'),
    path('auto/crear/', crear_auto, name='crear_auto'),
    path('auto/crear/moto/', crear_moto, name='crear_moto'),
    path('auto/crear/bicicleta/', crear_bicicleta, name='crear_bicicleta')
    
] 


  
