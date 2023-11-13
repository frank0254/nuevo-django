from django.contrib import admin
from inicio.models import Autos,Motos,Bicicletas
from usuarios.models import Datos
# Register your models here.

admin.site.register([Autos])
admin.site.register([Motos])
admin.site.register([Bicicletas])
admin.site.register([Datos])
