from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, DateTimeWidget
from import_export.admin import ImportExportModelAdmin
from django.utils import timezone
from .models import *

class CustomRegistroUsuarioResource(resources.ModelResource):
    tipo_contacto = fields.Field(column_name='Tipo Contacto', attribute='tipo_contacto')
    tipo_documento = fields.Field(column_name='Tipo Documento', attribute='tipo_documento')
    numero_documento = fields.Field(column_name='Número Documento', attribute='numero_documento')
    nombres = fields.Field(column_name='Nombres', attribute='nombres')
    apellidos = fields.Field(column_name='Apellidos', attribute='apellidos')
    fecha_registro = fields.Field(column_name='Fecha Registro', attribute='fecha_registro')
    sede_id = fields.Field(column_name='Sede ID', attribute='ip_sede', widget=ForeignKeyWidget(IpSede, 'sede__codigo_id'))
    departamento = fields.Field(column_name='Departamento', attribute='ip_sede', widget=ForeignKeyWidget(IpSede, 'sede__municipio__departamento__nombre'))
    municipio = fields.Field(column_name='Municipio', attribute='ip_sede', widget=ForeignKeyWidget(IpSede, 'sede__municipio__nombre'))
    direccion_ip = fields.Field(column_name='Dirección IP', attribute='ip_sede', widget=ForeignKeyWidget(IpSede, 'direccion_ip'))
    
    class Meta:
        model = RegistroUsuario
        fields = ('tipo_contacto', 'tipo_documento', 'numero_documento', 'nombres', 'apellidos', 'fecha_registro', 'sede_id', 'departamento', 'municipio', 'direccion_ip')

class CustomRegistroAccionUsuarioResource(resources.ModelResource):
    accion_nombre = fields.Field(column_name='Acción', attribute='accion', widget=ForeignKeyWidget(Accion, 'nombre'))
    fecha = fields.Field(column_name='Fecha acción', attribute='fecha')
    tipo_contacto = fields.Field(column_name='Tipo contacto', attribute='usuario', widget=ForeignKeyWidget(RegistroUsuario, 'tipo_contacto'))
    tipo_documento = fields.Field(column_name='Tipo documento', attribute='usuario', widget=ForeignKeyWidget(RegistroUsuario, 'tipo_documento'))
    numero_documento = fields.Field(column_name='Número documento', attribute='usuario', widget=ForeignKeyWidget(RegistroUsuario, 'numero_documento'))
    nombres = fields.Field(column_name='Nombres', attribute='usuario', widget=ForeignKeyWidget(RegistroUsuario, 'nombres'))
    apellidos = fields.Field(column_name='Apellidos', attribute='usuario', widget=ForeignKeyWidget(RegistroUsuario, 'apellidos'))
    sede_id = fields.Field(column_name='Sede ID', attribute='usuario', widget=ForeignKeyWidget(RegistroAccion, 'ip_sede__sede__codigo_id'))
    departamento = fields.Field(column_name='Departamento', attribute='usuario', widget=ForeignKeyWidget(RegistroAccion, 'ip_sede__sede__municipio__departamento__nombre'))
    municipio = fields.Field(column_name='Municipio', attribute='usuario', widget=ForeignKeyWidget(RegistroAccion, 'ip_sede__sede__municipio__nombre'))
    direccion_ip = fields.Field(column_name='Dirección IP', attribute='usuario', widget=ForeignKeyWidget(RegistroAccion, 'ip_sede__direccion_ip'))
    fecha_registro = fields.Field(column_name='Fecha registro', attribute='usuario', widget=ForeignKeyWidget(RegistroAccion, 'fecha_registro'))

    class Meta:
        model = RegistroAccionUsuario
        fields = ('accion_nombre','fecha','tipo_contacto','tipo_documento','numero_documento','nombres','apellidos','sede_id','departamento','municipio','direccion_ip','fecha_registro')

    def dehydrate_fecha_registro(self, registroAccionUsuario):
        if registroAccionUsuario.usuario is not None and registroAccionUsuario.usuario.fecha_registro is not None:
            return timezone.localtime(registroAccionUsuario.usuario.fecha_registro).strftime('%Y-%m-%d %H:%M:%S')
        return ''

    def dehydrate_fecha(self, registroAccionUsuario):
        if registroAccionUsuario.fecha is not None:
            return timezone.localtime(registroAccionUsuario.fecha).strftime('%Y-%m-%d %H:%M:%S')
        return '' 


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