from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from principal.views import *
from usuario.views import *
from principal.views import SMS

urlpatterns = [
    path("admin/", admin.site.urls),
    path('encuesta/', include(('encuesta.urls', 'encuesta'))),
    path('', IndexView, name="index"),
    path('panel/', PanelView, name="panel"),
    path('formajob/', Formajob, name="formajob"),
    path('gesples/', Gesples, name="gesples"),
    path('cercom/', Cercom, name="cercom"),
    path('setroc/', Setroc, name="setroc"),
    path('enrural/', Enrural, name="enrural"),
    # path('califica/', Califica, name="califica"),
    path('CampeSENA/', CAMPESENA, name="CampeSENA"),
    path('Bienestar/', BIENESTAR, name="Bienestar"),
    path('Servicios/', SERVICIOS, name="Servicios"),
    path('Empresarios/', EMPRESARIOS, name="Empresarios"),
    path('Pqr/', PQR, name="Pqr"),
    path('Catencion/', CATENCION, name="Catencion"),
    path('enviar_sms/', SMS, name="enviar_sms"),
    path('RegistroUser/', REGISTROUSER, name="RegistroUser"),
    # path('abrirUrl/<str:accion>/<path:url>', AbrirUrl, name="abrirUrl"),
    path('abrirUrl/<str:accion>/<str:url>/', AbrirUrl, name="abrirUrl"),
    #path("accounts/login/", Login, name="login"),
    #path('salir/', Logout, name='logout'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT_SERVER)

