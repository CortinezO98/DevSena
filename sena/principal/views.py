from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime
from .models import *

# Pagina principal
def IndexView(request):
    return render(request, "index.html")

@login_required
def PanelView(request):
    return render(request, "interface2.html")

@login_required
def Formajob(request):
    crearRegistroAccion(request, "Formación para el trabajo")
    return render(request, "formajob.html")

@login_required
def Gesples(request):
    crearRegistroAccion(request, "Gestión para el empleo Sena")
    return render(request, "gesples.html")

@login_required
def Cercom(request):
    crearRegistroAccion(request, "Certificación de competencias")
    return render(request, "cercom.html")

@login_required
def Setroc(request):
    crearRegistroAccion(request, "Senatronica")
    return render(request, "setroc.html")

@login_required
def Enrural(request):
    crearRegistroAccion(request, "Emprendimiento emprende rural")
    return render(request, "enrural.html")

@login_required
def Califica(request):
    if request.method == 'POST':
        encuesta = Encuesta(
            dominioPersonaAtendio = int(request.POST["dominioPersonaAtendio"]),
            satisfaccionServicioRecibido = int(request.POST["satisfaccionServicioRecibido"]),
            recomendacionCanalAtencion = int(request.POST["recomendacionCanalAtencion"]),
            solucionSolicitud = eval(request.POST["solucionSolicitud"]),
            ip = request.META.get('REMOTE_ADDR'),
            usuario = request.user if request.user else None
        )
        encuesta.save()
        messages.success(request, 'La encuesta de satisfacción se ha guardado correctamente.')
        return redirect('califica')
    return render(request, "califica.html")

@login_required
def AbrirUrl(request, accion, url):
    crearRegistroAccion(request, accion)
    return redirect(url)

def crearRegistroAccion(request, accion:str):
    registroAccion = RegistroAccion(
        accion = obtenerAccion(accion),
        ip = request.META.get('REMOTE_ADDR'),
        fecha = datetime.now(),
        usuario = request.user if request.user else None
    )
    registroAccion.save()
    
def obtenerAccion(nombre:str) -> Accion:
    accion = Accion.objects.filter(nombre=nombre).first()
    if not accion:
        accion = Accion(nombre=nombre)
        accion.save()
    return accion
        

