from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime
import base64
from .models import *
from .forms import RegistroFormulario
from .sms_utils import sms


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
    return render(request, "CampeSENA.html")


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
            registro.ip_dispositivo = obtenerIpCliente(request)
            registro.save()
            messages.success(request, 'Registro exitoso.')
            return redirect('panel') 
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
            ip = obtenerIpCliente(request),
            usuario = request.user if request.user.is_authenticated else None
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
        ip = obtenerIpCliente(request),
        fecha = datetime.now(),
        usuario = request.user if request.user.is_authenticated else None
    )
    registroAccion.save()
    
def obtenerIpCliente(request) -> str:
    ip_publica = request.META.get('REMOTE_ADDR')
    if 'HTTP_X_FORWARDED_FOR' in request.META:
        ip_publica = request.META['HTTP_X_FORWARDED_FOR'].split(',')[0].strip()
    return ip_publica
    
def obtenerAccion(nombre:str) -> Accion:
    accion = Accion.objects.filter(nombre=nombre).first()
    if not accion:
        accion = Accion(nombre=nombre)
        accion.save()
    return accion
        




def SMS(request):
    if request.method == "POST":
        numero_telefono = request.POST.get("numero_telefono")
        mensaje = "https://api.whatsapp.com/send/?phone=573168760255&text&app_absent=0"
        
        # Llama a la función para enviar SMS
        exito = sms(numero_telefono, mensaje)
        
        if exito:
            mensaje_confirmacion = "SMS enviado correctamente."
        else:
            mensaje_confirmacion = "Error al enviar el SMS. Por favor, inténtalo de nuevo."
            
        return render(request, "enviar_sms.html", {"mensaje_confirmacion": mensaje_confirmacion})
    else:
        return render(request, "enviar_sms.html")



def PanelView(request):
    mensaje_bienvenida = None
    if request.method == 'POST':
        form = RegistroFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombres']
            apellido = form.cleaned_data['apellidos']
            mensaje_bienvenida = f"{nombre} {apellido}"
            request.session['nombre_usuario'] = mensaje_bienvenida
    else:
        form = RegistroFormulario()
        mensaje_bienvenida = request.session.get('nombre_usuario', None)

    return render(request, "interface2.html", {'form': form, 'mensaje_bienvenida': mensaje_bienvenida})
