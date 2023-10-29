from django.urls import path
from inicio.views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('auto/', crear_auto,name='auto'), 
    path('moto/', crear_moto,name='moto'),
     path('bicicletas/', crear_bicicletas,name='biciletas')   
]
