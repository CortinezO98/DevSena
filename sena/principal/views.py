from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import messages
from django.db import transaction
from datetime import datetime
import base64
from .models import *
from .forms import RegistroFormulario, RegistroUsuarioForm
from .sms_utils import sms
import subprocess
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


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

@transaction.atomic
def REGISTROUSER(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            desea_senas = form.cleaned_data['desea_lengua_senas'] == 'True'
            request.session['sign_lang'] = desea_senas
            ipSede = ObtenerIpSede(request, request.POST["ip_sede"])
            try:
                with transaction.atomic():
                    registro = form.save(commit=False)
                    registro.fecha_registro = datetime.now()
                    registro.ip_sede = ipSede
                    registro.save()
                    request.session['usuarioActual'] = {
                        'id': registro.id,
                        'nombre': '{} {}'.format(registro.nombres, registro.apellidos),
                    }
                messages.success(request, 'Registro exitoso.')
            except Exception as ex:
                print("Exception: ", ex)
                messages.error(request, 'Ocurrió un error. Intente de nuevo.')
            
            response = redirect('/panel/')
            if not request.COOKIES.get('sedeId') or request.COOKIES.get('sedeId') != ipSede.sede.id:
                response.set_cookie('sedeId', ipSede.sede.id, max_age=315360000)  
            return response
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"Error en el campo {field}: {error}")
    else:
        sedes = Sede.objects.all()
        form = RegistroUsuarioForm()
    
    context = {
        'form': form, 
        'sedes': sedes,
        'ipSede': ObtenerIpSede(request, request.COOKIES.get('sedeId'))
    }
    return render(request, 'RegistroUser.html', context)

def ObtenerIpSede(request, sedeId):
    ip_cliente = obtenerIpCliente(request)
    ipSede = IpSede.objects.filter(direccion_ip=ip_cliente).first()
    sede = Sede.objects.filter(id=sedeId).first()
    if not ipSede and sede:
        ipSede = IpSede(
            direccion_ip=ip_cliente,
            sede_id=sedeId
        )
        ipSede.save()
    return ipSede

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
    usuarioActual = request.session.get('usuarioActual', None)
    registroAccion = RegistroAccionUsuario(
        accion = obtenerAccion(accion),
        fecha = datetime.now(),
        usuario_id = usuarioActual['id'] if usuarioActual else None
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
    usuarioActual = request.session.get('usuarioActual', None)
    print('usuarioActual', usuarioActual)
    if not usuarioActual:
        return redirect('RegistroUser')
    
    if request.session.get('sign_lang'):
        return render(request, 'panel_senas.html')
    
    return render(request, 'interface2.html')

def CerrarSesion(request):
    request.session['usuarioActual'] = None
    return redirect('index')



def lenguaje(request):
    return render(request, 'lenguaje.html')

def inscribete(request):
    return render(request, 'inscribete.html')

def egresados(request):
    return render(request, 'egresados.html')


def agenciaEmpleo(request):
    return render(request, 'agenciaEmpleo.html')


def formatos(request):
    return render(request, 'formatos.html')


def certificados(request):
    return render(request, 'certificados.html')

@csrf_exempt
def escanear_cedula(request):
    if request.method == 'POST':
        try:
            scanner_exe = r'C:\Program Files (x86)\Plustek\Plustek VTM300\VTM_Demo.exe'

            subprocess.Popen([scanner_exe], shell=True)

            return JsonResponse({'success': True})
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})
    return JsonResponse({'success': False, 'error': 'Método no permitido'})


def nosotros(request):
    return render(request, 'nosotros.html')