from django.urls import path
from . import views

urlpatterns = [
    path('GenerarLink/', views.GenerarLink, name='GenerarLink'),
    path('GenerarLink/<str:token>/', views.GenerarLinkRedirect, name='GenerarLinkRedirect'),
    path('Formulario/<str:token>/', views.Formulario, name='Formulario'),
    path('Finalizada/', views.Finalizada, name='Finalizada'),
] 