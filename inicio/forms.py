from django import forms
from ckeditor.fields import RichTextFormField

class BaseAutoFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = RichTextFormField()
    anio = forms.IntegerField()
    modelo = forms.CharField(max_length=300)
    fecha_de_creacion = forms.DateField(required=False)
    imagen_a_agregar = forms.ImageField(required=False) 


class CrearAutoFormulario(BaseAutoFormulario):
    ...

class ModificarAutoFormulario(BaseAutoFormulario):
    ...



class CrearMotoFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()
    modelo = forms.CharField(max_length=30)
    precio = forms.CharField(max_length=250)

class CrearBicicletaFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()

    