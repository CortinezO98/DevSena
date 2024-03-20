"""
URL configuration for sena project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from principal.views import *
from usuario.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', IndexView, name="index"),
    path('panel', PanelView, name="panel"),
    path('formajob', Formajob, name="formajob"),
    path('gesples', Gesples, name="gesples"),
    path('cercom', Cercom, name="cercom"),
    path('setroc', Setroc, name="setroc"),
    path('enrural', Enrural, name="enrural"),
    path('califica', Califica, name="califica"),
    path('CampeSENA', CAMPESENA, name="CampeSENA"),
    path('Bienestar', BIENESTAR, name="Bienestar"),
    path('Servicios', SERVICIOS, name="Servicios"),
    path('Empresarios', EMPRESARIOS, name="Empresarios"),
    path('Pqr', PQR, name="Pqr"),
    path('Catencion', CATENCION, name="Catencion"),
    path('RegistroUser/', REGISTROUSER, name="RegistroUser"),
    # path('abrirUrl/<str:accion>/<path:url>', AbrirUrl, name="abrirUrl"),
    path('abrirUrl/<str:accion>/<str:url>', AbrirUrl, name="abrirUrl"),
    path("accounts/login/", Login, name="login"),
    path('logout/', Logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
