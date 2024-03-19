from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from principal.views import crearRegistroAccion

def Login(request):
    if request.user.is_authenticated:
        return redirect('panel')
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            crearRegistroAccion(request, "Inicio de sesión")
            if request.GET.get('next'):
                return redirect(request.GET.get('next'))
            else:
                return redirect('index')
        else:
            messages.error(request, 'El usuario o la contraseña son incorrectos.')
            return redirect('login')
    else:
        return render(request, 'usuario/login.html')

def Logout(request):
    logout(request)
    return redirect('index')
