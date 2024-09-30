from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, routers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from .filterFacturaVarios import FacturaVariosFilter, PagoFacturaServicioFilter


from .models import FacturasVarios, PagoFacturasVarios, VariosF

from .serializers import VariosFSerializer, FacturaVariosSerializer, PagoFacturaVariosSerializer



class Varios_crud(viewsets.ModelViewSet):
    queryset = VariosF.objects.all().order_by('-id')
    serializer_class = VariosFSerializer
    router = routers.DefaultRouter()
    

class FacturaVarios_crud(viewsets.ModelViewSet):
    queryset = FacturasVarios.objects.all().order_by('-id')
    serializer_class = FacturaVariosSerializer
    router = routers.DefaultRouter()
    
    
class PagoFacturaVarios_crud(viewsets.ModelViewSet):
    queryset = PagoFacturasVarios.objects.all().order_by('-id')
    serializer_class = PagoFacturaVariosSerializer
    router = routers.DefaultRouter()
    


class FacturaVariosPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 2000

#vista para listar todas las facturas de servicios
class FacturaVarios_Filter(generics.ListAPIView):
   queryset = FacturasVarios.objects.all().order_by('-id')
   serializer_class = FacturaVariosSerializer
   pagination_class = FacturaVariosPagination
   filter_backends = [DjangoFilterBackend]
   filterset_class = FacturaVariosFilter
    
#vista para listar todos los facturas de servicios
class PagoFacturaVarios_Filter(generics.ListAPIView):
   queryset = PagoFacturasVarios.objects.all().order_by('-id')
   serializer_class = PagoFacturaVariosSerializer
   pagination_class = FacturaVariosPagination
   filter_backends = [DjangoFilterBackend]
   filterset_class = PagoFacturaServicioFilter
    