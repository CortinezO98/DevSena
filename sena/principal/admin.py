from django.contrib import admin
from django.http import HttpResponse
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportModelAdmin
from .models import *


class AccionResource(resources.ModelResource):
    class Meta:
        model = Accion

class AccionAdmin(ImportExportModelAdmin):
    resource_class = AccionResource
    
class DefaultRegistroAccionResource(resources.ModelResource):
    class Meta:
        model = RegistroAccion

class CustomRegistroAccionResource(resources.ModelResource):
    accion_nombre = fields.Field(
        column_name='Acción',
        attribute='accion',
        widget=ForeignKeyWidget(Accion, 'nombre'))
    
    datos_usuario = fields.Field(
        column_name='usuario',
        attribute='usuario',
        widget=ForeignKeyWidget(RegistroDatosUser, 'nombres'))
    class Meta:
        model = RegistroAccion
        fields = ('accion_nombre','ip','fecha','datos_usuario',)
            
class RegistroAccionAdmin(ImportExportModelAdmin):
    resource_class = DefaultRegistroAccionResource
    list_display = ('accion','ip','fecha')
    list_filter = ['fecha']
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        actions['export_custom'] = (self.export_custom, 'export_custom', 'Generar reporte de acciones')
        return actions

    def export_custom(self, request, queryset, modeladmin):
        resource = CustomRegistroAccionResource()
        dataset = resource.export(queryset, format='xlsx')
        response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="Reporte Acciones.xlsx"'
        return response

    export_custom.short_description = "Generar reporte de acciones"
        
class RegistroDatosUserResource(resources.ModelResource):
    class Meta:
        model = RegistroDatosUser
        
class RegistroDatosUserAdmin(ImportExportModelAdmin):
    resource_classes = [RegistroDatosUserResource]
    list_display = ('tipo_contacto','tipo_documento','numero_documento','nombres','apellidos','sede_contacto','ip_dispositivo','fecha_registro')
    search_fields = ['numero_documento','nombres','apellidos','sede_contacto','ip_dispositivo']
    list_filter = ['fecha_registro']

admin.site.register(Accion, AccionAdmin)
admin.site.register(RegistroAccion, RegistroAccionAdmin)
admin.site.register(RegistroDatosUser, RegistroDatosUserAdmin)
