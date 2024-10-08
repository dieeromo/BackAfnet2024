from django.shortcuts import render
from rest_framework import viewsets, routers
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import TipoCliente,NacionalidadCliente,Ciudad,Barrio,Comunidad
from .models import Cliente, Vivienda,ClienteVivienda, OrdenInstalacion
from .models import PlanClienteVivienda, Plan, Upgrade, OrdenCobro

from .serializers import TipoClienteSerializer,NacionalidadClienteSerializer,CiudadSerializer
from .serializers import BarrioSerializer,ComunidadSerializer,ClienteSerializer,ViviendaSerializer
from .serializers import ClienteViviendaSerializer, OrdenInstalacionSerializer
from .serializers import PlanClienteViviendaSerializer, PlanSerializer, UpgradeSerializer, OrdenCobroSerializer


class OrdenCobroViewSet(viewsets.ModelViewSet):
    queryset = OrdenCobro.objects.all()
    serializer_class = OrdenCobroSerializer
    router = routers.DefaultRouter()


class TipoClienteViewSet(viewsets.ModelViewSet):
    queryset = TipoCliente.objects.all()
    serializer_class = TipoClienteSerializer
    router = routers.DefaultRouter()

class NacionalidadClienteViewSet(viewsets.ModelViewSet):
    queryset = NacionalidadCliente.objects.all()
    serializer_class = NacionalidadClienteSerializer
    router = routers.DefaultRouter()
    
class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    router = routers.DefaultRouter()


    
class BarrioViewSet(viewsets.ModelViewSet):
    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    router = routers.DefaultRouter()
    
class GetBarrio_ciudad(APIView):
    def get(self,request):
        data=[]
        ciudad_id = request.query_params.get('ciudad_id', None)
        barrios = Barrio.objects.filter(ciudad=ciudad_id)
        for barrio_i in barrios:
            data.append({
                'nombre':barrio_i.nombre,
                'id':barrio_i.id
            })
        return Response(data)
    
class ComunidadViewSet(viewsets.ModelViewSet):
    queryset = Comunidad.objects.all()
    serializer_class = ComunidadSerializer
    router = routers.DefaultRouter()
    
class GetComunidad_ciudad(APIView):
    def get(self,request):
        data=[]
        ciudad_id = request.query_params.get('ciudad_id', None)
        barrios = Comunidad.objects.filter(ciudad=ciudad_id)
        for barrio_i in barrios:
            data.append({
                'nombre':barrio_i.nombre,
                'id':barrio_i.id
            })
        return Response(data)
    
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    router = routers.DefaultRouter()
    
class ViviendaViewSet(viewsets.ModelViewSet):
    queryset = Vivienda.objects.all()
    serializer_class = ViviendaSerializer
    router = routers.DefaultRouter()
    
class ClienteViviendaViewSet(viewsets.ModelViewSet):
    queryset = ClienteVivienda.objects.all().order_by('-id')
    serializer_class = ClienteViviendaSerializer
    router = routers.DefaultRouter()
    
    
class OrdenInstalacionViewSet(viewsets.ModelViewSet):
    queryset = OrdenInstalacion.objects.all()
    serializer_class = OrdenInstalacionSerializer
    router = routers.DefaultRouter()
    
    
class GetOrdenes_estado(APIView):
    def get(self,request):
        data=[]
        estado = request.query_params.get('estado_instalacion', None)
        ordenes = OrdenInstalacion.objects.filter(estado=estado).order_by('-id')
        for ordenes_i in ordenes:
            data.append({
                'id': ordenes_i.id,
                'nombresApellidos':ordenes_i.nombresApellidos,
                'cedula': ordenes_i.cedula,
                'telefono1': ordenes_i.telefono1,
                'telefono2': ordenes_i.telefono2,
                'email': ordenes_i.email,
                'tipoCliente':ordenes_i.tipoCliente.nombre,
                'tipoCliente_id':ordenes_i.tipoCliente.id,
                'tipoInstalacion':ordenes_i.tipoInstalacion,
                'nacionalidadCliente': ordenes_i.nacionalidadCliente.nombre,
                'nacionalidadCliente_id': ordenes_i.nacionalidadCliente.id,
                'fecha_solicitud':ordenes_i.fecha_solicitud.strftime('%d-%m-%Y %H:%M'),
                'fecha_instalacion':ordenes_i.fecha_instalacion,
                'direccion':ordenes_i.direccion,
                'estado':ordenes_i.estado, # 1 no Instalado, 2 Instalado, 3 Eliminado
                'digitador':ordenes_i.digitador.first_name,
            })
        return Response(data)
    
class GetClienteVivienda_cliente(APIView):
    def get(self,request):
        data=[]
        cliente_id = request.query_params.get('cliente_id', None)
        CV = ClienteVivienda.objects.filter(cliente=cliente_id, fecha_fin=None).order_by('-id')
        for CV_i in CV:
            data.append({
                'id':CV_i.id,
                'value':CV_i.id,
                'label':CV_i.vivienda.direccion,
                'vivienda_direccion':CV_i.vivienda.direccion,
                'vivienda_coordenadas':CV_i.vivienda.coordenadas,
                'vivienda_foto': str(CV_i.vivienda.foto) if  CV_i.vivienda else None,
                'vivienda_foto2': str(CV_i.vivienda.foto2) if  CV_i.vivienda else None,
                'vivienda_barrio':CV_i.vivienda.barrio.nombre if CV_i.vivienda.barrio else None,
                'ciudadBarrio':CV_i.vivienda.barrio.ciudad.nombre if CV_i.vivienda.barrio else None,
                'vivienda_comunidad': CV_i.vivienda.comunidad.nombre if CV_i.vivienda.comunidad else None,
                'ciudadComunidad':CV_i.vivienda.comunidad.ciudad.nombre if CV_i.vivienda.comunidad else None,
              
          
            })
        return Response(data)
    
    
class PlanClienteViviendaViewSet(viewsets.ModelViewSet):
    queryset = PlanClienteVivienda.objects.all()
    serializer_class = PlanClienteViviendaSerializer
    router = routers.DefaultRouter()
    
    
class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    router = routers.DefaultRouter()
    
def descripcion_de_estadoServicio(estadoServivio):
    estado=''
    if estadoServivio == 1:
        estado = 'Corriendo'
    if estadoServivio == 2:
        estado = 'Cortado'
    return estado
class GetPlan_ClienteVivienda_clienteVivienda(APIView):
    def get(self,request):
        data=[]
        clienteVivienda_id = request.query_params.get('clientevivienda_id', None)
        planes = PlanClienteVivienda.objects.filter(clienteVivienda=clienteVivienda_id)
        for planes_i in planes:
            
            data.append({
                'clienteID':planes_i.clienteVivienda.cliente.id,
                'planClienteViviendaID':planes_i.id,
                'clienteVivienda':planes_i.clienteVivienda.vivienda.direccion,
             
                'clienteViviendID':planes_i.clienteVivienda.id,
                'plan':planes_i.plan.nombre,
                'planID':planes_i.id,
                'fecha_instalacion':planes_i.fecha_instalacion,
                'fecha_pago':planes_i.fecha_pago,
                'estado':planes_i.estado,
                'estadoServcio':planes_i.estadoServicio,
                'estadoServicioDescripcion': descripcion_de_estadoServicio(planes_i.estadoServicio),
                'digitador':planes_i.digitador.first_name,
                'fecha_upgrade':planes_i.fecha_upgrade,
                
          
            })
        return Response(data)
    
    
class UpgradeViewSet(viewsets.ModelViewSet):
    queryset = Upgrade.objects.all()
    serializer_class = UpgradeSerializer
    router = routers.DefaultRouter()
    