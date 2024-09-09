from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, routers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .filtersFacturasServicios import FacturaSericioFilter,PagoFacturaServicioFilter


from .models import Servicio,FacturaServicios,PagoFacturasServicios

from .serializers import ServicioSerializer,FacturaServicioSerializer,PagoFacturaServicioSerializer



class Servicio_crud(viewsets.ModelViewSet):
    queryset = Servicio.objects.all().order_by('-id')
    serializer_class = ServicioSerializer
    router = routers.DefaultRouter()
    

class FacturaServicio_crud(viewsets.ModelViewSet):
    queryset = FacturaServicios.objects.all().order_by('-id')
    serializer_class = FacturaServicioSerializer
    router = routers.DefaultRouter()
    
    
class PagoFacturaServicio_crud(viewsets.ModelViewSet):
    queryset = PagoFacturasServicios.objects.all().order_by('-id')
    serializer_class = PagoFacturaServicioSerializer
    router = routers.DefaultRouter()
    


class FacturaServicioPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 2000

#vista para listar todas las facturas de servicios
class FacturaServicio_Filter(generics.ListAPIView):
   queryset = FacturaServicios.objects.all().order_by('-id')
   serializer_class = FacturaServicioSerializer
   pagination_class = FacturaServicioPagination
   filter_backends = [DjangoFilterBackend]
   filterset_class = FacturaSericioFilter
    
#vista para listar todos los facturas de servicios
class PagoFacturaServicio_Filter(generics.ListAPIView):
   queryset = PagoFacturasServicios.objects.all().order_by('-id')
   serializer_class = PagoFacturaServicioSerializer
   pagination_class = FacturaServicioPagination
   filter_backends = [DjangoFilterBackend]
   filterset_class = PagoFacturaServicioFilter
    