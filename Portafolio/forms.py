from django import forms

class ContactForm(forms.Form):
    Tipo_evento=forms.CharField(label="Tipo de Evento", empty_value="Todos",required="True")
    Fecha_inicio=forms.DateField(label="Fecha de inicio",required="True")
    Fecha_fin=forms.DateField(label="Fecha límite",required="True")
    Estado=forms.CharField(label="Estado",empty_value="Todos")
    Municipio=forms.CharField(label="Municipio",empty_value="Todos")
    Fuente=forms.CharField(label="Fuente",empty_value="Todos")