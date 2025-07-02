from django.shortcuts import render, redirect
from datetime import datetime, timedelta, timezone
from .models import *
import secrets
import string

def GenerarLink(request):
    if request.method == 'POST':
        caracteres = string.ascii_letters + string.digits
        encuesta = Encuesta(
            token = ''.join(secrets.choice(caracteres) for _ in range(10)),
            fechaExpiracionLink = datetime.now()  + timedelta(hours=24),
            nombreAgente = request.POST["nombreAgente"],
            idInteraccion = request.POST["idInteraccion"],
            seleccionarCanal = request.POST["seleccionarCanal"],
            fecha_creacion = datetime.now()
        )
        encuesta.save()
        return redirect('encuesta:GenerarLinkRedirect', encuesta.token)
    return render(request, 'encuesta/GenerarLink.html')

def GenerarLinkRedirect(request, token):
    dominio_actual = request.get_host()
    esquema = request.scheme
    encuestaLink = esquema + "://" + dominio_actual + "/encuesta/Formulario/" + token
    return render(request, 'encuesta/GenerarLink.html', {'encuestaLink': encuestaLink})

def Formulario(request, token):
    encuesta = Encuesta.objects.filter(token=token).first()
    if request.method == 'POST':
        encuesta.dominioPersonaAtendio = int(request.POST["dominioPersonaAtendio"])
        encuesta.satisfaccionServicioRecibido = int(request.POST["satisfaccionServicioRecibido"])
        encuesta.tiempoEsperaServicio = int(request.POST["tiempoEsperaServicio"])
        encuesta.recomendacionCanalAtencion = int(request.POST["recomendacionCanalAtencion"])
        encuesta.fechaExpiracionLink = datetime.now()
        encuesta.save()
        return redirect('encuesta:Finalizada')
    else:
        if encuesta and encuesta.fechaExpiracionLink.astimezone(timezone.utc) >= datetime.now(timezone.utc):
            return render(request, 'encuesta/Formulario.html')
        else:
            return render(request, 'encuesta/expiroLink.html')
        
def Finalizada(request):
    return render(request, 'encuesta/encuestaFinalizada.html')
        

