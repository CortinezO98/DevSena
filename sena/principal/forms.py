from django import forms
from .models import RegistroDatosUser

class RegistroFormulario(forms.ModelForm):
    TIPO_CONTACTO_CHOICES = (
        ('', 'Selecciona una opción'),
        ('CIUDADANO', 'CIUDADANO'),
        ('EMPRESARIO', 'EMPRESARIO'),
    )
    TIPO_DOCUMENTO_CHOICES = (
        ('', 'Selecciona una opción'),
        ('CARNET_DIPLOMATICO', 'CARNET DIPLOMATICO'),
        ('CEDULA_CIUDADANIA', 'CÉDULA CIUDADANIA'),
        ('CEDULA_EXTRANJERA', 'CÉDULA EXTRANJERA'),
        ('NIT', 'NIT'),
        ('PASAPORTE', 'PASAPORTE'),
        ('PEP', 'PEP'),
        ('PPT', 'PPT'),
        ('REGISTRO_CIVIL', 'REGISTRO CIVIL'),
        ('TARJETA_IDENTIDAD', 'TARJETA IDENTIDAD')
    )

    SEDE_CONTACTO_CHOICES = (
        ('', 'Selecciona una opción'),
        ('ANTIOQUIA_CAUCASIA', 'ANTIOQUIA-CAUCASIA'),
        ('ANTIOQUIA_MEDELLÍN', 'ANTIOQUIA-MEDELLÍN'),
        ('ARAUCA_ARAUCA', 'ARAUCA-ARAUCA'),
        ('ATLÁNTICO_BARRANQUILLA', 'ATLÁNTICO-BARRANQUILLA'),
        ('CAQUETÁ_FLORENCIA', 'CAQUETÁ-FLORENCIA'),
        ('CAUCA_SANTANDER_DE_QUILICHAO', 'CAUCA-SANTANDER DE QUILICHAO'),
        ('CUNDINAMARCA_BOGOTÁ D.C', 'CUNDINAMARCA-BOGOTÁ D.C'),
        ('CUNDINAMARCA_SOACHA', 'CUNDINAMARCA-SOACHA'),
        ('GUAINÍA_PUERTO_INÍRIDA', 'GUAINÍA-PUERTO INÍRIDA'),
        ('GUAVIARE_SAN_JOSE_DEL_GUAVIARE', 'GUAVIARE-SAN JOSE DEL GUAVIARE'),
        ('LA_GUAJIRA_FONSECA', 'LA GUAJIRA-FONSECA'),
        ('LA_GUAJIRA_MAICAO', 'LA GUAJIRA-MAICAO'),
        ('MAGDALENA_CIENAGA', 'MAGDALENA-CIENAGA'),
        ('META_GRANADA', 'META-GRANADA'),
        ('META_PUERTO_GAITÁN', 'META-PUERTO GAITÁN'),
        ('META_VILLAVICENCIO', 'META-VILLAVICENCIO'),
        ('NARIÑO_PASTO', 'NARIÑO-PASTO'),
        ('NEIVA_HUILA', 'NEIVA-HUILA'),
        ('PUTUMAYO_PUERTO_ASÍS', 'PUTUMAYO PUERTO ASÍS'),
        ('QUINDIO_ARMENIA', 'QUINDIO-ARMENIA'),
        ('RISARALDA_DOSQUEBRADAS', 'RISARALDA-DOSQUEBRADAS'),
        ('SAN_ANDRÉS_Y_PROVIDENCIA_SAN_ANDRÉS', 'SAN ANDRÉS Y PROVIDENCIA-SAN ANDRÉS'),
        ('VALLE_DEL_CAUCA_BUGA', 'VALLE DEL CAUCA-BUGA')
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
