from django.shortcuts import render
from rest_framework import viewsets, routers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from django.db.models import Prefetch

from .serializers import PuertoTarjetaSerializer

from .modelsCuartoEquipos import PuertoTarjeta
from .modelsTrazos import Trazo2, Trazo3
from .serializers import Trazo2Serializer
#############

class PuertoTarjetaViewSet(viewsets.ModelViewSet):
    queryset = PuertoTarjeta.objects.all()
    serializer_class = PuertoTarjetaSerializer
    router = routers.DefaultRouter()

#############

# Create your views here.

class TrazoListView(APIView):
    def get(self, request):
        paginator = PageNumberPagination()
        paginator.page_size = 10  # Puedes ajustar el tamaño de página según tus necesidades

        trazos = Trazo2.objects.select_related(
            'sal_trazo1__sal_trazoPatchcord__sal_puertoTarjeta__tarjeta__olt',
            'sal_trazo1__sal_trazoPatchcord__lleg_puertoODF',
            'sal_trazo1__hiloTrazado',
            'sal_trazo1__hiloSalida',
            'lleg_Mufa',
            'lleg_Caja',
            'hiloTrazado',
            'hiloSalida'
        ).prefetch_related(
            Prefetch(
                'trazo3_set',
                queryset=Trazo3.objects.select_related(
                    'lleg_Mufa',
                    'lleg_Caja',
                    'hiloTrazado',
                    'hiloSalida'
                )
            )
        ).all()
        
        page = paginator.paginate_queryset(trazos, request)
        serializer = Trazo2Serializer(page, many=True)
        return paginator.get_paginated_response(serializer.data)
        
