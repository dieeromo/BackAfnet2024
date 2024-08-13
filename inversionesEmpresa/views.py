from rest_framework import viewsets, routers
from .models import Inversion, Diversificacion, Retiro, Destino, SubDestino
from .serializers import InversionSerializer, DiversificacionSerializer, RetiroSerializer
from rest_framework.response import Response
from rest_framework.decorators import action

from librouteros import connect
from django.http import JsonResponse


def conectar_mikrotik(request):
    try:
        # Datos de conexión
        host = '192.168.11.80'
        username = 'admin'
        password = 'qpal1234.'
        
        # Conectar a MikroTik
        api = connect(username=username, password=password, host=host)
        
        # Realizar una consulta simple, por ejemplo, obtener la lista de interfaces

        interfaces = list( api('/ip/route/print'))
        response_data = {'status': 'success', 'interfaces': interfaces}
 
        
    except Exception as e:
        response_data = {'status': 'error', 'message': str(e)}
    
    return JsonResponse(response_data)


class InversionViewSet(viewsets.ModelViewSet):


    queryset = Inversion.objects.all()
    serializer_class = InversionSerializer

    @action(detail=True, methods=['post'])
    def agregar_diversificacion(self, request, pk=None):
        inversion = self.get_object()
        data = request.data
        destino = Destino.objects.get(id= 1)  ## OJO AQUI
        diversificacion = Diversificacion.objects.create(
            inversion=inversion,
            destino=destino,
            porcentaje=data['porcentaje'],
            valor_inversion=data['valor_inversion'],
            valor_rendimiento=data['valor_rendimiento']
        )
        diversificacion.save()
        inversion.save()
        print('SSSSALIDA')
        return Response({'status': 'diversificacion agregada'})
    
    
class DiversificacionViewSet(viewsets.ModelViewSet):
    queryset = Diversificacion.objects.all()
    serializer_class = DiversificacionSerializer
    

    @action(detail=True, methods=['post'])
    def agregar_retiro(self, request, pk=None):
        diversificacion = self.get_object()
        data = request.data
        subDestino = SubDestino.objects.get(id=data['subDestino'])
        retiro = Retiro.objects.create(
            diversificacion=diversificacion,
            descripcion=data['descripcion'],
            subDestino = subDestino,
            valor=data['valor'],
            fecha=data['fecha']
        )
        retiro.save()
        diversificacion.inversion.save()
        return Response({'status': 'retiro agregado'})
    
class InversionViewSet2(viewsets.ModelViewSet):

    queryset = Inversion.objects.all()
    serializer_class = InversionSerializer
    router = routers.DefaultRouter()