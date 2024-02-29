from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime

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

