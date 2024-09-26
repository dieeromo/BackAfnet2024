from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, routers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from cliente.serializers import ClienteViviendaSerialize_filter_NapAP

from .models import RouterMK,AP_nodos,Mikrotik_PlanClienteVivienda
from .serializers import RouterMKSerializer,AP_nodosSerializer,Mikrotik_PlanClienteViviendaSerializer
from .filters import Mikrotik_PlanClienteVivienda_Filter

class RouterMK_Crud_View(viewsets.ModelViewSet):
    queryset = RouterMK.objects.all()
    serializer_class = RouterMKSerializer
    router = routers.DefaultRouter()
    
class AP_nodos_Crud_View(viewsets.ModelViewSet):
    queryset = AP_nodos.objects.all()
    serializer_class = AP_nodosSerializer
    router = routers.DefaultRouter()
    
class Mikrotik_PlanClienteVivienda_Crud_View(viewsets.ModelViewSet):
    queryset = Mikrotik_PlanClienteVivienda.objects.all()
    serializer_class = Mikrotik_PlanClienteViviendaSerializer
    router = routers.DefaultRouter()
    
    
    
class MikrotikPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 2000

class Mikrotik_PlanCliente_View(generics.ListAPIView):
   queryset = Mikrotik_PlanClienteVivienda.objects.all().order_by('-id')
   serializer_class = Mikrotik_PlanClienteViviendaSerializer
   pagination_class = MikrotikPagination
   filter_backends = [DjangoFilterBackend]
   filterset_class = Mikrotik_PlanClienteVivienda_Filter
   
   
class AP_nodos_FilterViewSet(viewsets.ModelViewSet):
    queryset = AP_nodos.objects.all()
    serializer_class = AP_nodosSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    
    # Campos para realizar búsquedas por nombre del AP y SSID
    search_fields = ['nombre', 'ssid']
    
    # Filtro para filtrar por ID o nombre del router relacionado
    filterset_fields = {
        'router__id': ['exact'],
        'router__nombre': ['icontains','exact'],
        # 'nombre':['exact', 'icontains'],
        # 'ssid':['exact', 'icontains'],
    }
    
    # Permite ordenar por la frecuencia
    ordering_fields = ['frecuencia','ipv4']
   
   


class ClientesConectadosCajaNapView(APIView):
    def get(self, request, caja_nap_id):
        # Obtener los planes de clientes vinculados a esta CajaNap
        conexiones = Mikrotik_PlanClienteVivienda.objects.filter(caja_id=caja_nap_id).select_related(
            'planCliente__clienteVivienda__cliente',
            'planCliente__clienteVivienda__vivienda__barrio',
            'planCliente__clienteVivienda__vivienda__comunidad',
            'planCliente__plan'
        )

        # Serializar los datos
        resultado = []
        for conexion in conexiones:
            cliente_vivienda = conexion.planCliente.clienteVivienda
            plan = conexion.planCliente.plan.nombre
            data = {
                "cliente": cliente_vivienda.cliente.nombresApellidos,
                "barrio": cliente_vivienda.vivienda.barrio.nombre if cliente_vivienda.vivienda.barrio else None,
                "comunidad": cliente_vivienda.vivienda.comunidad.nombre if cliente_vivienda.vivienda.comunidad else None,
                "direccion": cliente_vivienda.vivienda.direccion,
                "plan": plan,
                "ipv4": conexion.ipv4_address
            }
            resultado.append(data)

        return Response(resultado)
    
    
class ClientesConectados_AP_View(APIView):
    def get(self, request, ap_id):
        # Obtener los planes de clientes vinculados a esta CajaNap
        conexiones = Mikrotik_PlanClienteVivienda.objects.filter(ap_id=ap_id).select_related(
            'planCliente__clienteVivienda__cliente',
            'planCliente__clienteVivienda__vivienda__barrio',
            'planCliente__clienteVivienda__vivienda__comunidad',
            'planCliente__plan'
        )

        # Serializar los datos
        resultado = []
        for conexion in conexiones:
            cliente_vivienda = conexion.planCliente.clienteVivienda
            plan = conexion.planCliente.plan.nombre
            data = {
                "cliente": cliente_vivienda.cliente.nombresApellidos,
                "barrio": cliente_vivienda.vivienda.barrio.nombre if cliente_vivienda.vivienda.barrio else None,
                "comunidad": cliente_vivienda.vivienda.comunidad.nombre if cliente_vivienda.vivienda.comunidad else None,
                "direccion": cliente_vivienda.vivienda.direccion,
                "plan": plan,
                "ipv4": conexion.ipv4_address
            }
            resultado.append(data)

        return Response(resultado)