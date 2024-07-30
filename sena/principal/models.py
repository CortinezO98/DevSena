from django.db import models
from django.contrib.auth.models import User


class Accion(models.Model):
    nombre = models.CharField(max_length=150)
    class Meta:
        verbose_name = 'Acción'
        verbose_name_plural = 'Acciones'
    def __str__(self):
        return "{}".format(self.nombre)
    
class RegistroDatosUser(models.Model):
    tipo_contacto = models.CharField(max_length=20)
    tipo_documento = models.CharField(max_length=50)
    numero_documento = models.CharField(max_length=10)
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    sede_contacto = models.CharField(max_length=100)
    ip_dispositivo = models.CharField(max_length=100)
    fecha_registro = models.DateTimeField(null=True)

    def __str__(self):
        return f'{self.nombres} {self.apellidos}'
    
class RegistroAccion(models.Model):
    accion = models.ForeignKey(Accion, on_delete=models.CASCADE)
    ip = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(RegistroDatosUser, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = 'Registro de acción'
        verbose_name_plural = 'Registro de acciones'
    def __str__(self):
        return "{} - {} - {} - {}".format(self.id, self.accion.nombre, self.ip, self.usuario, self.fecha)