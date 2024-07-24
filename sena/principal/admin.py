from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class RegistroAccionResource(resources.ModelResource):
    class Meta:
        model = RegistroAccion
        
class RegistroAccionAdmin(ImportExportModelAdmin):
    resource_classes = [RegistroAccionResource]
    list_display = ('accion','ip','fecha')
    list_filter = ['fecha'] 
        
class RegistroDatosUserResource(resources.ModelResource):
    class Meta:
        model = RegistroDatosUser
        
class RegistroDatosUserAdmin(ImportExportModelAdmin):
    resource_classes = [RegistroDatosUserResource]
    list_display = ('tipo_contacto','tipo_documento','numero_documento','nombres','apellidos','sede_contacto','ip_dispositivo','fecha_registro')
    search_fields = ['numero_documento','nombres','apellidos','sede_contacto','ip_dispositivo']
    list_filter = ['fecha_registro']

admin.site.register(Accion)
admin.site.register(RegistroAccion, RegistroAccionAdmin)
admin.site.register(RegistroDatosUser, RegistroDatosUserAdmin)
