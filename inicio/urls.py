from django.urls import path
from inicio.views import inicio, auto, moto, bicicletas, crear_auto, crear_moto, crear_bicicleta, eliminar_auto, modificar_auto
from inicio.views import detalle_auto







urlpatterns = [
    path('', inicio, name='inicio'),
    path('auto/',auto,name='auto'), 
    path('moto/',moto,name='moto'),
    path('bicicletas/',bicicletas,name='biciletas'),
    path('auto/crear/', crear_auto, name='crear_auto'),
    path('auto/crear/moto/', crear_moto, name='crear_moto'),
    path('auto/crear/bicicleta/', crear_bicicleta, name='crear_bicicleta'),
   path('auto/<int:auto_id>/', detalle_auto, name= 'detalle_auto'),
    path('auto/<int:auto_id>/eliminar/', eliminar_auto, name= 'eliminar_auto'),  
    path('auto/<int:auto_id>/modificar/', modificar_auto, name= 'modificar_auto'),
] 


  
