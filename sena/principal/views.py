from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime

# Pagina principal
def IndexView(request):
    return render(request, "index.html")

def Interface2(request):
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

