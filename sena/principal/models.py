from django.db import models

class ClickLog(models.Model):
    boton = models.CharField(max_length=100)
    usuario = models.CharField(max_length=100)
    fecha = models.DateTimeField()
