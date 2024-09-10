from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import conectar_mikrotik, firewall_cortar
from .views2 import cortar_usuario, habilitar_usuario


urlpatterns = [

    path('conectar/', conectar_mikrotik,),
    path('cortar/', firewall_cortar,),
    path('cortar_usuario/', cortar_usuario,),
    path('habilitar_usuario/', habilitar_usuario,),
  
]
