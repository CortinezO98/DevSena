from django.db import models

class Encuesta(models.Model):
    dominioPersonaAtendio = models.IntegerField(null=True, blank=True)
    satisfaccionServicioRecibido = models.IntegerField(null=True, blank=True)
    recomendacionCanalAtencion = models.IntegerField(null=True, blank=True)
    solucionSolicitud = models.BooleanField(null=True, blank=True)
    idInteraccion = models.CharField(max_length=150)
    seleccionarCanal = models.CharField(max_length=150, null=True, blank=True)
    nombreAgente = models.CharField(max_length=150)
    token = models.CharField(max_length=50)
    fechaExpiracionLink = models.DateTimeField()