from django import forms
from .models import RegistroDatosUser

class RegistroFormulario(forms.ModelForm):
    TIPO_CONTACTO_CHOICES = (
        ('ciudadano', 'Ciudadano'),
        ('empresario', 'Empresario'),
    )
    TIPO_DOCUMENTO_CHOICES = (
        ('cedula_ciudadania', 'Cédula ciudadanía'),
        ('cedula_extranjeria', 'Cédula extranjería'),
        ('carnet_diplomatico', 'Carnet diplomático'),
        ('pasaporte', 'Pasaporte'),
        ('pep', 'PEP'),
        ('ppt', 'PPT'),
        ('registro_civil', 'Registro civil'),
        ('tarjeta_identidad', 'Tarjeta de identidad'),
        ('nit', 'NIT'),
    )

    tipo_contacto = forms.ChoiceField(choices=TIPO_CONTACTO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    tipo_documento = forms.ChoiceField(choices=TIPO_DOCUMENTO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    numero_documento = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10'}))
    nombres = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '20'}))
    apellidos = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '20'}))
    sede_contacto = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = RegistroDatosUser
        fields = ['tipo_contacto', 'tipo_documento', 'numero_documento', 'nombres', 'apellidos', 'sede_contacto']
        error_messages = {
            'tipo_contacto': {'required': 'Este campo es requerido'},
            'tipo_documento': {'required': 'Este campo es requerido'},
            'numero_documento': {'required': 'Este campo es requerido'},
            'nombres': {'required': 'Este campo es requerido'},
            'apellidos': {'required': 'Este campo es requerido'},
            'sede_contacto': {'required': 'Este campo es requerido'},
        }
