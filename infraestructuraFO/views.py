from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, routers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MufaFilter

# Create your views here.
from .modelsCajasMufas import Mufa, CajaNap
from .modelsCuarto import OLT, TarjetaOLT,PuertoTarjeta,ODF,PuertoODF,TrazoPachcord
from .modelsTrazos import TipoFibra,CableFibra,HiloFibra,Trazo1,Trazo2,Trazo3

from .serializers import Trazo3Serializer,Trazo2Serializer,Trazo1Serializer
from .serializers import HiloFibraSerializer,CableFibraSerializer,TipoFibraSerializer
from .serializers import TrazoPatchcordSerializer,ODFSerializer,PuertoTarjetaSerializer
from .serializers import TarjetaOLTSerializer,OLTSerializer,MufaSerializer,CajaNapSerializer


class InfraestructuraFOPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 2000

    
class MufaListFilter_View(generics.ListAPIView):
   queryset = Mufa.objects.all().order_by('-id')
   serializer_class = MufaSerializer
   pagination_class = InfraestructuraFOPagination
   filter_backends = [DjangoFilterBackend]
   filterset_class = MufaFilter
    

class MufaViewSet(viewsets.ModelViewSet):
    queryset = Mufa.objects.all()
    serializer_class = MufaSerializer
    router = routers.DefaultRouter()
    

    
    
class CajaNapViewSet(viewsets.ModelViewSet):
    queryset = CajaNap.objects.all()
    serializer_class = CajaNapSerializer
    router = routers.DefaultRouter()
    