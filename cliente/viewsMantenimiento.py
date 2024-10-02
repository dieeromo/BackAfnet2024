from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, routers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required
from datetime import datetime

from django.http import JsonResponse

from . modelsMantenimiento import QuejaCliente, DiagnosticoPreliminar
from . modelsMantenimiento import DiagnosticoInSitu, SolucionQuejaCliente
from . modelsMantenimiento import Mantenimiento
from . modelsMantenimiento import SolicitudesCliente,RespuestasSolicitudesCliente
from . modelsMantenimiento import AtencionSolicitudesCliente

from . serializersMantenimiento import QuejaCliente_Serializer, DiagnosticoPreliminar_Serializer
from . serializersMantenimiento import DiagnosticoInSitu_Serializer, SolucionQuejaCliente_Serializer
from . serializersMantenimiento import Mantenimiento_Serializer, SolicitudesCliente_Serializer
from . serializersMantenimiento import RespuestaSolicitudesCliente_Serializer, AtencionSolicitudesCliente_Serializer


class QuejaCliente_crud(viewsets.ModelViewSet):
    queryset = QuejaCliente.objects.all()
    serializer_class = QuejaCliente_Serializer
    router = routers.DefaultRouter()
    
class DiagnosticoPreliminar_crud(viewsets.ModelViewSet):
    queryset = DiagnosticoPreliminar.objects.all()
    serializer_class = DiagnosticoPreliminar_Serializer
    router = routers.DefaultRouter()

class DiagnosticoInSitu_crud(viewsets.ModelViewSet):
    queryset = DiagnosticoInSitu.objects.all()
    serializer_class = DiagnosticoInSitu_Serializer
    router = routers.DefaultRouter()
    
class SolucionQuejaCliente_crud(viewsets.ModelViewSet):
    queryset = SolucionQuejaCliente.objects.all()
    serializer_class = SolucionQuejaCliente_Serializer
    router = routers.DefaultRouter()
    
class Mantenimiento_crud(viewsets.ModelViewSet):
    queryset = Mantenimiento.objects.all()
    serializer_class = Mantenimiento_Serializer
    router = routers.DefaultRouter()


class SolicitudesCliente_crud(viewsets.ModelViewSet):
    queryset = SolicitudesCliente.objects.all()
    serializer_class = SolicitudesCliente_Serializer
    router = routers.DefaultRouter()
    
class RespuestaSolicitudesCliente_crud(viewsets.ModelViewSet):
    queryset = RespuestasSolicitudesCliente.objects.all()
    serializer_class = RespuestaSolicitudesCliente_Serializer
    router = routers.DefaultRouter()
    
class AtencionSolicitudesCliente_crud(viewsets.ModelViewSet):
    queryset = AtencionSolicitudesCliente.objects.all()
    serializer_class = AtencionSolicitudesCliente_Serializer
    router = routers.DefaultRouter()
    
    
