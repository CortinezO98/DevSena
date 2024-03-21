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
        ('ANTIOQUIA-CAUCASIA', 'ANTIOQUIA-CAUCASIA'),
        ('ANTIOQUIA-MEDELLÍN', 'ANTIOQUIA-MEDELLÍN'),
        ('ARAUCA-ARAUCA', 'ARAUCA-ARAUCA'),
        ('ATLÁNTICO-BARRANQUILLA', 'ATLÁNTICO-BARRANQUILLA'),
        ('CAQUETÁ-FLORENCIA', 'CAQUETÁ-FLORENCIA'),
        ('CAUCA-SANTANDER DE QUILICHAO', 'CAUCA-SANTANDER DE QUILICHAO'),
        ('CUNDINAMARCA-BOGOTÁ D.C', 'CUNDINAMARCA-BOGOTÁ D.C'),
        ('CUNDINAMARCA-SOACHA', 'CUNDINAMARCA-SOACHA'),
        ('GUAINÍA-PUERTO INÍRIDA', 'GUAINÍA-PUERTO INÍRIDA'),
        ('GUAVIARE- SAN JOSE DEL GUAVIARE', 'GUAVIARE- SAN JOSE DEL GUAVIARE'),
        ('LA GUAJIRA-FONSECA', 'LA GUAJIRA-FONSECA'),
        ('LA GUAJIRA-MAICAO', 'LA GUAJIRA-MAICAO'),
        ('MAGDALENA-CIENAGA', 'MAGDALENA-CIENAGA'),
        ('META-GRANADA', 'META-GRANADA'),
        ('META-PUERTO GAITÁN', 'META-PUERTO GAITÁN'),
        ('META-VILLAVICENCIO', 'META-VILLAVICENCIO'),
        ('NARIÑO-PASTO', 'NARIÑO-PASTO'),
        ('NEIVA-HUILA', 'NEIVA-HUILA'),
        ('PUTUMAYO_PUERTO ASÍS', 'PUTUMAYO_PUERTO ASÍS'),
        ('QUINDIO-ARMENIA', 'QUINDIO-ARMENIA'),
        ('RISARALDA-DOSQUEBRADAS', 'RISARALDA-DOSQUEBRADAS'),
        ('SAN ANDRÉS Y PROVIDENCIA-SAN ANDRÉS', 'SAN ANDRÉS Y PROVIDENCIA-SAN ANDRÉS'),
        ('VALLE DEL CAUCA-BUGA', 'VALLE DEL CAUCA-BUGA')
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
