from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from .models import *

class EncuestaResource(resources.ModelResource):
    # Personalizar campos con títulos específicos
    token = fields.Field(attribute='token', column_name='Token de Encuesta')
    dominioPersonaAtendio = fields.Field(attribute='dominioPersonaAtendio', column_name='Facilidad de contacto')
    satisfaccionServicioRecibido = fields.Field(attribute='satisfaccionServicioRecibido', column_name='Claridad de la informacion')
    tiempoEsperaServicio = fields.Field(attribute='tiempoEsperaServicio', column_name='Calidad de la informacion')
    recomendacionCanalAtencion = fields.Field(attribute='recomendacionCanalAtencion', column_name='Tiempo de espera')
    # solucionSolicitud = fields.Field(attribute='solucionSolicitud', column_name='Solución a la Solicitud')
    idInteraccion = fields.Field(attribute='idInteraccion', column_name='idInteraccion')
    seleccionarCanal = fields.Field(attribute='seleccionarCanal', column_name='seleccionarCanal')
    nombreAgente = fields.Field(attribute='nombreAgente', column_name='nombreAgente')
    fechaExpiracionLink = fields.Field(attribute='fechaExpiracionLink', column_name='fechaExpiracionLink')
    fecha_creacion = fields.Field(attribute='fecha_creacion', column_name='fecha_creacion')

    class Meta:
        model = Encuesta
        # Definir el orden de las columnas en el export
        export_order = (
            'token',
            'nombreAgente', 
            'idInteraccion',
            'seleccionarCanal',
            'dominioPersonaAtendio',
            'satisfaccionServicioRecibido',
            'tiempoEsperaServicio',
            'recomendacionCanalAtencion',
            'solucionSolicitud',
            'fecha_creacion',
            'fechaExpiracionLink'
        )
        
class EncuestaAdmin(ImportExportModelAdmin):
    resource_classes = [EncuestaResource]
    list_display = ('token','dominioPersonaAtendio','satisfaccionServicioRecibido','tiempoEsperaServicio', 'recomendacionCanalAtencion', 'nombreAgente','idInteraccion','seleccionarCanal','fecha_creacion','fechaExpiracionLink',)
    list_filter = ('fecha_creacion','seleccionarCanal')
    
admin.site.register(Encuesta, EncuestaAdmin)