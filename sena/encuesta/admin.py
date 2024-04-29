from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class EncuestaResource(resources.ModelResource):
    class Meta:
        model = Encuesta
        
class EncuestaAdmin(ImportExportModelAdmin):
    resource_classes = [EncuestaResource]
    list_display = ('dominioPersonaAtendio','satisfaccionServicioRecibido', 'recomendacionCanalAtencion', 'solucionSolicitud',)

admin.site.register(Encuesta, EncuestaAdmin)