from django import forms
from django.forms import ModelForm

from libros.models import Libro, Autor


class ContactanosForm(forms.Form):
    asunto = forms.CharField(max_length=100)
    mensaje = forms.CharField()
    remitente = forms.EmailField()
    reenviar_remitente = forms.BooleanField(required=False) 


class AutorForm(ModelForm):
    class Meta:
        model = Autor


class LibroForm(ModelForm):
    class Meta:
        model = Libro