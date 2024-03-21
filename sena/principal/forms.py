from django import forms
from .models import RegistroDatosUser

class RegistroFormulario(forms.ModelForm):
    TIPO_CONTACTO_CHOICES = (
        ('', 'Selecciona una opción'),
        ('ciudadano', 'Ciudadano'),
        ('empresario', 'Empresario'),
    )
    TIPO_DOCUMENTO_CHOICES = (
        ('', 'Selecciona una opción'),
        ('cedula_ciudadania', 'Cédula ciudadanía'),
        ('cedula_extranjera', 'Cédula extranjera'),
        ('carnet_diplomatico', 'Carnet diplomático'),
        ('pasaporte', 'Pasaporte'),
        ('pep', 'PEP'),
        ('ppt', 'PPT'),
        ('registro_civil', 'Registro civil'),
        ('tarjeta_identidad', 'Tarjeta de identidad'),
        ('nit', 'NIT'),
    )

    SEDE_CONTACTO_CHOICES = (
        ('', 'Selecciona una opción'),
        ('Antioquia-Medellín', 'Antioquia-Medellín'),
        ('ATLÁNTICO-BARRANQUILLA', 'ATLÁNTICO-BARRANQUILLA'),
        ('NEIVA-HUILA', 'NEIVA-HUILA'),
        ('VALLE DEL CAUCA-BUGA', 'VALLE DEL CAUCA-BUGA'),
        ('CUNDINAMARCA-BOGOTÁ D.C', 'CUNDINAMARCA-BOGOTÁ D.C'),
        ('CUNDINAMARCA-SOACHA', 'CUNDINAMARCA-SOACHA'),
        ('MAGDALENA-CIENAGA', 'MAGDALENA-CIENAGA'),
        ('META-VILLAVICENCIO', 'META-VILLAVICENCIO'),
        ('META-PUERTO GAITÁN', 'META-PUERTO GAITÁN'),
        ('META-GRANADA', 'META-GRANADA'),
        ('NARIÑO-PASTO', 'NARIÑO-PASTO'),
        ('QUINDIO-ARMENIA', 'QUINDIO-ARMENIA'),
        ('RISARALDA-DOSQUEBRADAS', 'RISARALDA-DOSQUEBRADAS'),
        ('LA GUAJIRA-MAICAO', 'LA GUAJIRA-MAICAO'),
        ('LA GUAJIRA-FONSECA', 'LA GUAJIRA-FONSECA'),
        ('GUAVIARE- SAN JOSE DEL GUAVIARE', 'GUAVIARE- SAN JOSE DEL GUAVIARE'),
        ('PUTUMAYO_PUERTO ASÍS', 'PUTUMAYO_PUERTO ASÍS'),
        ('SAN ANDRÉS Y PROVIDENCIA-SAN ANDRÉS', 'SAN ANDRÉS Y PROVIDENCIA-SAN ANDRÉS'),
        ('ANTIOQUIA-CAUCASIA', 'ANTIOQUIA-CAUCASIA'),
        ('ARAUCA-ARAUCA', 'ARAUCA-ARAUCA'),
        ('CAQUETÁ-FLORENCIA', 'CAQUETÁ-FLORENCIA'),
        ('CAUCA-SANTANDER DE QUILICHAO', 'CAUCA-SANTANDER DE QUILICHAO'),
        ('GUAINÍA-PUERTO INÍRIDA', 'GUAINÍA-PUERTO INÍRIDA'),
    )

    tipo_contacto = forms.ChoiceField(choices=TIPO_CONTACTO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    tipo_documento = forms.ChoiceField(choices=TIPO_DOCUMENTO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    numero_documento = forms.CharField(max_length=10, widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '10'}))
    nombres = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '20'}))
    apellidos = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control', 'maxlength': '20'}))
    sede_contacto = forms.ChoiceField(choices=SEDE_CONTACTO_CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))

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
