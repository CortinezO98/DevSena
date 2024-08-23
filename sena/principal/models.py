from django.db import models
from django.contrib.auth.models import User

class Accion(models.Model):
    nombre = models.CharField(max_length=150)
    class Meta:
        verbose_name = 'Acción'
        verbose_name_plural = 'Acciones'
    def __str__(self):
        return "{}".format(self.nombre)

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self):
        return "{}".format(self.nombre)

class Municipio(models.Model):
    nombre = models.CharField(max_length=100)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    def __str__(self):
        return "{}".format(self.nombre)

class Sede(models.Model):
    codigo_id = models.CharField(max_length=10)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    def __str__(self):
        return "{} {}".format(self.codigo_id, self.municipio.nombre)
    def nombre(self):
        return "{}-{}".format(self.municipio.nombre, self.municipio.departamento.nombre)

class IpSede(models.Model):
    direccion_ip = models.CharField(max_length=100)
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    def __str__(self):
        return "{} - {}".format(self.sede.nombre(), self.direccion_ip)      

class RegistroUsuario(models.Model):
    TIPO_CONTACTO_CHOICES = [
        ('CIUDADANO', 'CIUDADANO'),
        ('EMPRESARIO', 'EMPRESARIO')
    ]
    TIPO_DOCUMENTO_CHOICES = [
        ('CARNET_DIPLOMATICO', 'CARNET DIPLOMATICO'),
        ('CEDULA_CIUDADANIA', 'CÉDULA CIUDADANIA'),
        ('CEDULA_EXTRANJERA', 'CÉDULA EXTRANJERA'),
        ('NIT', 'NIT'),
        ('PASAPORTE', 'PASAPORTE'),
        ('PEP', 'PEP'),
        ('PPT', 'PPT'),
        ('REGISTRO_CIVIL', 'REGISTRO CIVIL'),
        ('TARJETA_IDENTIDAD', 'TARJETA IDENTIDAD')
    ]
    tipo_contacto = models.CharField(max_length=20, choices=TIPO_CONTACTO_CHOICES)
    tipo_documento = models.CharField(max_length=50, choices=TIPO_DOCUMENTO_CHOICES)
    numero_documento = models.CharField(max_length=10)
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    fecha_registro = models.DateTimeField(null=True)
    ip_sede = models.ForeignKey(IpSede, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'

class RegistroAccionUsuario(models.Model):
    accion = models.ForeignKey(Accion, on_delete=models.CASCADE)
    fecha = models.DateTimeField(null=True)
    usuario = models.ForeignKey(RegistroUsuario, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = 'Registro acción'
        verbose_name_plural = 'Registro acciones'
    def __str__(self):
        return "{} - {} {}".format(self.id, self.accion.nombre, self.fecha)

class RegistroDatosUser(models.Model):
    tipo_contacto = models.CharField(max_length=20)
    tipo_documento = models.CharField(max_length=50)
    numero_documento = models.CharField(max_length=10)
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    sede_contacto = models.CharField(max_length=100)
    ip_dispositivo = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(null=True)
    class Meta:
        verbose_name = 'Registro datos usuario (anterior)'
        verbose_name_plural = 'Registro datos usuarios (anterior)'
    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
    
class RegistroAccion(models.Model):
    accion = models.ForeignKey(Accion, on_delete=models.CASCADE)
    ip = models.CharField(max_length=100)
    fecha = models.DateTimeField(null=True)
    usuario = models.ForeignKey(RegistroDatosUser, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = 'Registro acción (anterior)'
        verbose_name_plural = 'Registro acciones (anterior)'
    def __str__(self):
        return "{} - {} - {} - {}".format(self.id, self.accion.nombre, self.ip, self.usuario, self.fecha)

