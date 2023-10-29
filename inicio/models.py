from django.db import models

# Create your models here.
class Autos(models.Model):
    marca = models.CharField(max_length=30)
    descripcion = models.TextField()
    anio = models.IntegerField()
    
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