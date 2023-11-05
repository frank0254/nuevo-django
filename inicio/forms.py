from django import forms

class BaseAutoFormulario(forms.Form):
    marca = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=250)
    anio = forms.IntegerField()
    


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

    