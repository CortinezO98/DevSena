from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime
import base64
from .models import *
from .forms import RegistroFormulario

# Pagina principal
def IndexView(request):
    return render(request, "index.html")


def PanelView(request):
    return render(request, "interface2.html")


def Formajob(request):
    return render(request, "formajob.html")


def Gesples(request):
    return render(request, "gesples.html")


def Cercom(request):
    return render(request, "cercom.html")


def Setroc(request):
    return render(request, "setroc.html")


def Enrural(request):
    return render(request, "enrural.html")


def CAMPESENA(request):
    return render(request, "campeSENA.html")


def BIENESTAR(request):
    return render(request, "Bienestar.html")


def SERVICIOS(request):
    return render(request, "Servicios.html")


def EMPRESARIOS(request):
    return render(request, "Empresarios.html")


def PQR(request):
    return render(request, "Pqr.html")


def CATENCION(request):
    return render(request, "Catencion.html")



def REGISTROUSER(request):
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            registro = form.save(commit=False)
            registro.ip_dispositivo = request.META.get('REMOTE_ADDR')
            registro.save()
            messages.success(request, 'Registro exitoso.')
            return redirect('panel')  # Reemplaza 'panel' con el nombre de la URL de tu página de éxito
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en el campo {field}: {error}")
    else:
        form = RegistroFormulario()
        
    return render(request, 'RegistroUser.html', {'form': form})


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

# 
# def AbrirUrl(request, accion, url):
#     crearRegistroAccion(request, accion)
#     return redirect(url)


def AbrirUrl(request, accion, url):
    crearRegistroAccion(request, accion)
    return redirect(validarUrl(url))

def validarUrl(url) -> str:
    url = url.replace('_', '/')
    try:
        return base64.b64decode(url).decode()
    except:
        return url

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
        

