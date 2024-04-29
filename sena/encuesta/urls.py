from django.urls import path
from . import views

urlpatterns = [
    path('GenerarLink/', views.GenerarLink, name='GenerarLink'),
    path('Formulario/<str:token>/', views.Formulario, name='Formulario'),
    path('Finalizada/', views.Finalizada, name='Finalizada'),
] 