from django.contrib import admin
from django.http import HttpResponse
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateTimeWidget
from django.utils import timezone
from import_export.admin import ImportExportModelAdmin
from .models import *
from .customReports import *


class AccionResource(resources.ModelResource):
    class Meta:
        model = Accion

class AccionAdmin(ImportExportModelAdmin):
    resource_class = AccionResource

class DepartamentoResource(resources.ModelResource):
    class Meta:
        model = Departamento

class DepartamentoAdmin(ImportExportModelAdmin):
    resource_class = DepartamentoResource

class MunicipioResource(resources.ModelResource):
    class Meta:
        model = Municipio

class MunicipioAdmin(ImportExportModelAdmin):
    resource_class = MunicipioResource

class SedeResource(resources.ModelResource):
    class Meta:
        model = Sede

class SedeAdmin(ImportExportModelAdmin):
    resource_class = SedeResource

class IpSedeResource(resources.ModelResource):
    class Meta:
        model = IpSede

class IpSedeAdmin(ImportExportModelAdmin):
    resource_class = IpSedeResource

class RegistroUsuarioResource(resources.ModelResource):
    class Meta:
        model = RegistroUsuario

class RegistroUsuarioAdmin(ImportExportModelAdmin):
    resource_class = RegistroUsuarioResource
    list_display = ('numero_documento','nombres','apellidos','ip_sede',)
    search_fields = ['numero_documento']

    def get_actions(self, request):
        actions = super().get_actions(request)
        actions['export_custom'] = (self.export_custom, 'export_custom', 'Generar reporte de registro usuarios')
        return actions

    def export_custom(self, request, queryset, modeladmin):
        resource = CustomRegistroUsuarioResource()
        dataset = resource.export(queryset, format='xlsx')
        response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="Reporte registro usuarios.xlsx"'
        return response

    export_custom.short_description = "Generar reporte de registro usuarios"

class RegistroAccionUsuarioResource(resources.ModelResource):
    class Meta:
        model = RegistroAccionUsuario

class RegistroAccionUsuarioAdmin(ImportExportModelAdmin):
    resource_class = RegistroAccionUsuarioResource
    list_display = ('accion','usuario','fecha',)
    list_filter = ['fecha']
    search_fields = ['fecha','usuario','accion',]
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        actions['export_custom'] = (self.export_custom, 'export_custom', 'Generar reporte de acciones')
        return actions

    def export_custom(self, request, queryset, modeladmin):
        resource = CustomRegistroAccionUsuarioResource()
        dataset = resource.export(queryset, format='xlsx')
        response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="Reporte Acciones.xlsx"'
        return response

    export_custom.short_description = "Generar reporte de acciones"

class DefaultRegistroAccionResource(resources.ModelResource):
    class Meta:
        model = RegistroAccion
        
class RegistroAccionAdmin(ImportExportModelAdmin):
    resource_class = DefaultRegistroAccionResource
    list_display = ('accion','ip','fecha')
    list_filter = ['fecha']
    
    def get_actions(self, request):
        actions = super().get_actions(request)
        actions['export_custom'] = (self.export_custom, 'export_custom', 'Generar reporte acciones')
        return actions

    def export_custom(self, request, queryset, modeladmin):
        resource = CustomRegistroAccionResource()
        dataset = resource.export(queryset, format='xlsx')
        response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="Reporte Acciones.xlsx"'
        return response

    export_custom.short_description = "Generar reporte acciones"
        
class RegistroDatosUserResource(resources.ModelResource):
    class Meta:
        model = RegistroDatosUser
        
class RegistroDatosUserAdmin(ImportExportModelAdmin):
    resource_classes = [RegistroDatosUserResource]
    list_display = ('tipo_contacto','tipo_documento','numero_documento','nombres','apellidos','sede_contacto','ip_dispositivo','fecha_registro')
    search_fields = ['numero_documento','nombres','apellidos','sede_contacto','ip_dispositivo']
    list_filter = ['fecha_registro']

admin.site.register(Accion, AccionAdmin)
admin.site.register(Departamento, DepartamentoAdmin)
admin.site.register(Municipio, MunicipioAdmin)
admin.site.register(Sede, SedeAdmin)
admin.site.register(IpSede, IpSedeAdmin)
admin.site.register(RegistroUsuario, RegistroUsuarioAdmin)
admin.site.register(RegistroAccionUsuario, RegistroAccionUsuarioAdmin)
admin.site.register(RegistroAccion, RegistroAccionAdmin)
admin.site.register(RegistroDatosUser, RegistroDatosUserAdmin)
