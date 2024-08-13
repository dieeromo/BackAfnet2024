from django.shortcuts import render
from rest_framework import viewsets, routers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Caja,ProveedorEquipo,ModoCompra,ModoPagoProveedor
from .models import Presupuesto,FacturaEquipo,PagoFacturasEquipos

from .serializers import CajaSerializer,ProveedorEquipoSerializer
from .serializers import ModoCompraSerializer, ModoPagoProveedorSerializer
from .serializers import PresupuestoSerializer,FacturaEquipoSerializer
from .serializers import PagoFacturaEquiposSerializer

class CajaViewSet(viewsets.ModelViewSet):
    queryset = Caja.objects.all()
    serializer_class = CajaSerializer
    router = routers.DefaultRouter()

class ProveedorEquipoViewSet(viewsets.ModelViewSet):
    queryset = ProveedorEquipo.objects.all()
    serializer_class = ProveedorEquipoSerializer
    router = routers.DefaultRouter()
    
class ModoCompraViewSet(viewsets.ModelViewSet):
    queryset = ModoCompra.objects.all()
    serializer_class = ModoCompraSerializer
    router = routers.DefaultRouter()

class ModoPagoProveedorViewSet(viewsets.ModelViewSet):
    queryset = ModoPagoProveedor.objects.all()
    serializer_class = ModoPagoProveedorSerializer
    router = routers.DefaultRouter()

class PresupuestoViewSet(viewsets.ModelViewSet):
    queryset = Presupuesto.objects.all()
    serializer_class = PresupuestoSerializer
    router = routers.DefaultRouter()

class FacturaEquipoViewSet(viewsets.ModelViewSet):
    queryset = FacturaEquipo.objects.all().order_by('-id')
    serializer_class = FacturaEquipoSerializer
    router = routers.DefaultRouter()
    
class PagoFacturaEquipoViewSet(viewsets.ModelViewSet):
    queryset = PagoFacturasEquipos.objects.all()
    serializer_class = PagoFacturaEquiposSerializer
    router = routers.DefaultRouter()


