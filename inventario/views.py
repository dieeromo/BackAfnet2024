from django.shortcuts import render
from rest_framework import viewsets, routers
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import TipoEquipo,Homologado,Bodega,Equipo
from .models import EquipoMovimientoBodega,EquipoInstalado

from . serializers import TipoEquipoSerializer, HomologadoSerializer
from . serializers import BodegaSerializer,EquipoSerializer
from . serializers import EquipoMovimientoBodegaSerializer,EquipoInstaladoSerializer


class TipoEquipoViewSet(viewsets.ModelViewSet):
    queryset = TipoEquipo.objects.all()
    serializer_class = TipoEquipoSerializer
    router = routers.DefaultRouter()
    
class HomologadoViewSet(viewsets.ModelViewSet):
    queryset = Homologado.objects.all()
    serializer_class = TipoEquipoSerializer
    router = routers.DefaultRouter()
    
class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Bodega.objects.all()
    serializer_class = BodegaSerializer
    router = routers.DefaultRouter()
    
class EquipoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.all().order_by('-id')
    serializer_class = EquipoSerializer
    router = routers.DefaultRouter()
    
#VISTA QUE DEVUELVE LOS EQUIPOS QUE NO ESTAN INSTALADOS NI VENDIDOS NI DA˜NADOS
class ListaEquipo_NoInstalatoViewSet(viewsets.ModelViewSet):
    queryset = Equipo.objects.filter(estado2=1).exclude(estado=3)
    serializer_class = EquipoSerializer
    router = routers.DefaultRouter()
    

class EquipoMovimientoBodegaViewSet(viewsets.ModelViewSet):
    queryset = EquipoMovimientoBodega.objects.all()
    serializer_class = EquipoMovimientoBodegaSerializer
    router = routers.DefaultRouter()

class EquipoInstaladoViewSet(viewsets.ModelViewSet):
    queryset = EquipoInstalado.objects.all()
    serializer_class = EquipoInstaladoSerializer
    router = routers.DefaultRouter()
    
class GetEquipoInstaladoActivo_Plan(APIView):
    def get(self,request):
        data=[]
        planClienteVivienda_id = request.query_params.get('plan_cliente_vivienda_id', None)
        equipos = EquipoInstalado.objects.filter(planClienteVivienda=planClienteVivienda_id,estado=1)
        for equipos_i in equipos:
            data.append({
                'nombreName':equipos_i.equipo.homologado.nombre +" "+ equipos_i.equipo.serie,
                'estado':equipos_i.estado, # estado activo inactivo
                'condicion_equipo': equipos_i.equipo.estado,
                'id':equipos_i.id,
                'fecha_instalacion':equipos_i.fecha_instalacion
            })
        return Response(data)