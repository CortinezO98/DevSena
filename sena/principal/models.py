from django.db import models
from django.contrib.auth.models import User

class AccionRegistro(models.Model):
    accion = models.CharField(max_length=100)
    ip = models.CharField(max_length=100)
    fecha = models.DateTimeField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
