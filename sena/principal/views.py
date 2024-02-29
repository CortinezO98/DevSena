from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
#from django.http import HttpResponse
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
    return render(request, "formajob.html")

@login_required
def Gesples(request):
    return render(request, "gesples.html")

@login_required
def Cercom(request):
    return render(request, "cercom.html")

@login_required
def Setroc(request):
    return render(request, "setroc.html")

@login_required
def Enrural(request):
    return render(request, "enrural.html")

@login_required
def Califica(request):
    return render(request, "califica.html")

def crearRegistroAccion(request, accion):
    usuario = request.user if request.user else None
    accionRegistro = AccionRegistro(
        accion = accion,
        ip = request.META.get('REMOTE_ADDR'),
        fecha = datetime.now(),
        usuario = usuario
        
    )
    accionRegistro.save()

