from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import *

class AccionResource(resources.ModelResource):
    class Meta:
        model = Accion
        
class AccionAdmin(ImportExportModelAdmin):
    resource_classes = [AccionResource]
    list_display = ('id','nombre',)
    search_fields = ['id','nombre']

class RegistroAccionResource(resources.ModelResource):
    class Meta:
        model = RegistroAccion
        
class RegistroAccionAdmin(ImportExportModelAdmin):
    resource_classes = [RegistroAccionResource]
    list_display = ('accion','usuario','ip','fecha')
    search_fields = ['fecha'] 
        
class RegistroDatosUserResource(resources.ModelResource):
    class Meta:
        model = RegistroDatosUser
        
class RegistroDatosUserAdmin(ImportExportModelAdmin):
    resource_classes = [RegistroDatosUserResource]
    list_display = ('tipo_contacto','tipo_documento','numero_documento','nombres','apellidos','sede_contacto','ip_dispositivo',)
    search_fields = ['numero_documento','nombres','apellidos','sede_contacto','ip_dispositivo']

admin.site.register(Accion, AccionAdmin)
admin.site.register(RegistroAccion, RegistroAccionAdmin)
admin.site.register(RegistroDatosUser, RegistroDatosUserAdmin)
