from django.contrib import admin
from django.http import HttpResponse
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateTimeWidget
from django.utils import timezone
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
    
    tipo_contacto = fields.Field(
        column_name='Tipo Contacto',
        attribute='usuario',
        widget=ForeignKeyWidget(RegistroDatosUser, 'tipo_contacto'))
    
    tipo_documento = fields.Field(
        column_name='Tipo Documento',
        attribute='usuario',
        widget=ForeignKeyWidget(RegistroDatosUser, 'tipo_documento'))
    
    numero_documento = fields.Field(
        column_name='Número Documento',
        attribute='usuario',
        widget=ForeignKeyWidget(RegistroDatosUser, 'numero_documento'))
    
    nombres = fields.Field(
        column_name='Nombres',
        attribute='usuario',
        widget=ForeignKeyWidget(RegistroDatosUser, 'nombres'))
    
    apellidos = fields.Field(
        column_name='Apellidos',
        attribute='usuario',
        widget=ForeignKeyWidget(RegistroDatosUser, 'apellidos'))
    
    sede_contacto = fields.Field(
        column_name='Sede Contacto',
        attribute='usuario',
        widget=ForeignKeyWidget(RegistroDatosUser, 'sede_contacto'))
    
    ip_dispositivo = fields.Field(
        column_name='IP Dispositivo',
        attribute='usuario',
        widget=ForeignKeyWidget(RegistroDatosUser, 'ip_dispositivo'))
    
    fecha_registro = fields.Field(
        column_name='Fecha Registro',
        attribute='usuario',
        widget=DateTimeWidget(format='%Y-%m-%d %H:%M:%S'))
    
    fecha = fields.Field(
        column_name='Fecha de accion',
        attribute='fecha',
        widget=DateTimeWidget(format='%Y-%m-%d %H:%M:%S'))
    
    class Meta:
        model = RegistroAccion
        fields = ('accion_nombre', 'tipo_contacto', 'tipo_documento', 'numero_documento', 'nombres', 'apellidos', 'sede_contacto', 'ip_dispositivo', 'fecha_registro')

    def dehydrate_fecha_registro(self, registroaccion):
        if registroaccion.usuario is not None and registroaccion.usuario.fecha_registro is not None:
            return timezone.localtime(registroaccion.usuario.fecha_registro).strftime('%Y-%m-%d %H:%M:%S')
        return ''

    def dehydrate_fecha(self, registroaccion):
        if registroaccion.fecha is not None:
            return timezone.localtime(registroaccion.fecha).strftime('%Y-%m-%d %H:%M:%S')
        return ''    
        
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
