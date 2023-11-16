from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone


# Create your models here.
class Autos(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = RichTextField()
    anio = models.IntegerField()    
    modelo =models.CharField(max_length=30, null=True)
    fecha_de_creacion = models.DateField(default=timezone.now)
    imagen_a_agregar = models.ImageField(upload_to='avatares', null=True, blank=True)
    
    def __str__(self):  
        return f' {self.id} - {self.marca} - {self.anio}'
    
    

class Motos(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    anio = models.IntegerField()
    
    def __str__(self):
        return f' {self.id} - {self.marca} - {self.anio}'
    



class Bicicletas(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    anio = models.IntegerField()
    
    def __str__(self):
        return f' {self.id} - {self.marca} - {self.anio}'