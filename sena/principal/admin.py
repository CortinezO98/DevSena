from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django.http import HttpResponse
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateTimeWidget
from django.utils import timezone
from import_export.admin import ImportExportModelAdmin
from .models import *
from .customReports import *
import datetime



class MonthYearFilter(SimpleListFilter):
    title = 'Mes y Año'
    parameter_name = 'month_year'

    def lookups(self, request, model_admin):
        qs = model_admin.get_queryset(request)
        dates = qs.exclude(fecha__isnull=True).order_by('fecha').values_list('fecha', flat=True)
        months = {(d.year, d.month) for d in dates if d is not None}
        lookups = [
            (f"{year}-{month:02d}", datetime.date(year, month, 1).strftime("%B %Y"))
            for year, month in months
        ]
        return sorted(lookups, reverse=True)

    def queryset(self, request, queryset):
        if self.value():
            try:
                year, month = map(int, self.value().split('-'))
                start_date = timezone.make_aware(datetime.datetime(year, month, 1))
                if month == 12:
                    end_date = timezone.make_aware(datetime.datetime(year + 1, 1, 1))
                else:
                    end_date = timezone.make_aware(datetime.datetime(year, month + 1, 1))
                return queryset.filter(fecha__gte=start_date, fecha__lt=end_date)
            except Exception as e:
                print("Error en el filtro MonthYearFilter:", e)
                return queryset
        return queryset








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
    list_display = ('numero_documento', 'nombres', 'apellidos', 'ip_sede')
    search_fields = ['numero_documento']

    @admin.action(description="Generar reporte de registro usuarios")
    def export_custom(self, request, queryset):
        resource = CustomRegistroUsuarioResource()
        dataset = resource.export(queryset, format='xlsx')
        response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="Reporte registro usuarios.xlsx"'
        return response

    actions = [export_custom]

class RegistroAccionUsuarioResource(resources.ModelResource):
    class Meta:
        model = RegistroAccionUsuario

class RegistroAccionUsuarioAdmin(ImportExportModelAdmin):
    resource_class = RegistroAccionUsuarioResource
    list_display = ('accion', 'usuario', 'fecha')
    list_filter = [MonthYearFilter]
    search_fields = ['fecha', 'usuario', 'accion']

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('accion', 'usuario').only('accion', 'usuario', 'fecha')

    @admin.action(description="Generar reporte de acciones")
    def export_custom(self, request, queryset):
        queryset = queryset.filter(fecha__gte="2025-01-01").only("accion", "usuario", "fecha")
        resource = CustomRegistroAccionUsuarioResource()
        dataset = resource.export(queryset, format='xlsx')
        response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="Reporte Acciones.xlsx"'
        return response

    actions = [export_custom]


class DefaultRegistroAccionResource(resources.ModelResource):
    class Meta:
        model = RegistroAccion

class RegistroAccionAdmin(ImportExportModelAdmin):
    resource_class = DefaultRegistroAccionResource
    list_display = ('accion', 'ip', 'fecha')
    list_filter = ['fecha']

    @admin.action(description="Generar reporte acciones")
    def export_custom(self, request, queryset):
        resource = CustomRegistroAccionResource()
        dataset = resource.export(queryset, format='xlsx')
        response = HttpResponse(dataset.xlsx, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename="Reporte Acciones.xlsx"'
        return response

    actions = [export_custom]

class RegistroDatosUserResource(resources.ModelResource):
    class Meta:
        model = RegistroDatosUser

class RegistroDatosUserAdmin(ImportExportModelAdmin):
    resource_class = RegistroDatosUserResource
    list_display = ('tipo_contacto', 'tipo_documento', 'numero_documento', 'nombres', 'apellidos', 'sede_contacto', 'ip_dispositivo', 'fecha_registro')
    search_fields = ['numero_documento', 'nombres', 'apellidos', 'sede_contacto', 'ip_dispositivo']
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
