from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, routers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status

from django.db.models import Count, Q
from .models import EquipoInstalado
from .serializers import EquipoInstaladoSerializer
from .models import Equipo
from .models import EquipoInstalado, EquipoMovimientoBodega
from .serializers import EquipoInstaladoSerializer, EquipoMovimientoBodegaSerializer
from . serializers import EquipoSerializer

from .filters import EquiposInstaladoFilter
class GeneralPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 2000

class GetEquipoListFilter_View(generics.ListAPIView):
    queryset = Equipo.objects.all().order_by('-id')
    serializer_class = EquipoSerializer
    pagination_class = GeneralPagination
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados pueden acceder
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]  # Agrega capacidad de ordenar y filtrar
    search_fields = ['serie']  # Filtra por el campo 'serie'
    filterset_fields = ['homologado','estado','estado2','bodega']  # Permite filtrar por 'homologado' y 'estado2'
    ordering_fields = ['serie', 'precio_compra']  # Permite ordenar por 'serie' y 'precio_compra'
    ordering = ['-id']  # Ordena por defecto por 'id' descendente
    
    
# class EstadisticaEquipos_View(APIView):
#     def get(self, request):
#         equipos_por_bodega = Equipo.objects.values('bodega__nombre').annotate(total=Count('id')).order_by('-total')
#         equipos_por_homologado = Equipo.objects.values('homologado__nombre').annotate(total=Count('id')).order_by('-total')
#         equipos_por_estado = Equipo.objects.values('estado').annotate(total=Count('id')).order_by('-total')
#         equipos_con_estado2_igual_a_1 = Equipo.objects.filter(estado2=1).count()
        
#         equipos_por_bodega_nuevo = Equipo.objects.values('bodega__nombre','homologado__nombre').filter(estado=1,estado2=1).annotate(total=Count('id')).order_by('-total')
#         equipos_por_bodega_usado = Equipo.objects.values('bodega__nombre','homologado__nombre').filter(estado=2,estado2=1).annotate(total=Count('id')).order_by('-total')
#         equipos_por_bodega_revisar = Equipo.objects.values('bodega__nombre','homologado__nombre').filter(estado=4,estado2=1).annotate(total=Count('id')).order_by('-total')
#         equipos_por_bodega_dañado = Equipo.objects.values('bodega__nombre','homologado__nombre').filter(estado=3,estado2=1).annotate(total=Count('id')).order_by('-total')
        
#         equipos_por_bodega_todos = Equipo.objects.values('bodega__nombre','homologado__nombre').filter(estado2=1).annotate(total=Count('id')).order_by('-total')
#         equipos_todos = Equipo.objects.values('homologado__nombre','estado').filter(estado2=1).annotate(total=Count('id')).order_by('-total')
#         equipos_todos_local = Equipo.objects.values('homologado__nombre','estado').filter(estado2=1, bodega=1).annotate(total=Count('id')).order_by('-total')
#         data = {
#             #'equipos_por_bodega': list(equipos_por_bodega),
#             #'equipos_por_homologado': list(equipos_por_homologado),
#             #'equipos_por_estado': list(equipos_por_estado),
#             #'equipos_con_estado2_igual_a_1': equipos_con_estado2_igual_a_1,
            
#             #'equipos_por_bodega_nuevo':list(equipos_por_bodega_nuevo),
#             #'equipos_por_bodega_usado':list(equipos_por_bodega_usado),
#             #'equipos_por_bodega_revisar':list(equipos_por_bodega_revisar),
#             #'equipos_por_bodega_dañado':list(equipos_por_bodega_dañado),
#             #'equipos_por_bodega_todos ':list(equipos_por_bodega_todos ),
#             'equipos_todos':list(equipos_todos ),
#             #'equipos_todos_local':list(equipos_todos_local),
#         }
#         return Response(data)
    
    
# class EstadisticaEquiposGeneral_View(APIView):
#     def get(self, request):
#         # Anotaciones para contar cada estado en base al homologado
#         equipos_por_homologado = Equipo.objects.values('homologado__nombre').annotate(
#             nuevo_count=Count('id', filter=Q(estado=1)),
#             usado_count=Count('id', filter=Q(estado=2)),
#             danado_count=Count('id', filter=Q(estado=3)),
#             revisar_count=Count('id', filter=Q(estado=4)),
#         ).order_by('homologado__nombre')

#         # Estructura personalizada del JSON
#         data = []
#         for item in equipos_por_homologado:
#             homologado_data = {
#                 'homologado': item['homologado__nombre'],
#                 'estados': {
#                     'Nuevo': item['nuevo_count'],
#                     'Usado': item['usado_count'],
#                     'Dañado': item['danado_count'],
#                     'Revisar': item['revisar_count'],
#                 }
#             }
#             data.append(homologado_data)

#         return Response(data)
    
class EquipoCountView(APIView):
    def get(self, request):
        homologado_filter = request.GET.get('homologado', None)

        equipos_por_homologado = Equipo.objects.values('homologado__nombre')

        if homologado_filter:
            equipos_por_homologado = equipos_por_homologado.filter(homologado__nombre__icontains=homologado_filter)

        equipos_por_homologado = equipos_por_homologado.annotate(
            nuevo_count=Count('id', filter=Q(estado=1)),
            usado_count=Count('id', filter=Q(estado=2)),
            danado_count=Count('id', filter=Q(estado=3)),
            revisar_count=Count('id', filter=Q(estado=4)),
        ).order_by('homologado__nombre')

        data = []
        for item in equipos_por_homologado:
            homologado_data = {
                'homologado': item['homologado__nombre'],
                'estados': {
                    'Nuevo': item['nuevo_count'],
                    'Usado': item['usado_count'],
                    'Dañado': item['danado_count'],
                    'Revisar': item['revisar_count'],
                }
            }
            data.append(homologado_data)

        return Response(data)




class EquipoCount_bodega_View(APIView):
    def get(self, request):
        homologado_filter = request.GET.get('homologado', None)

        equipos = Equipo.objects.all()

        if homologado_filter:
            equipos = equipos.filter(homologado__nombre__icontains=homologado_filter)

        # Agrupación por homologado y luego por bodega
        agrupacion = equipos.values('homologado__nombre', 'bodega__nombre').annotate(
            nuevo_count=Count('id', filter=Q(estado=1)),
            usado_count=Count('id', filter=Q(estado=2)),
            danado_count=Count('id', filter=Q(estado=3)),
            revisar_count=Count('id', filter=Q(estado=4)),
        ).order_by('homologado__nombre', 'bodega__nombre')

        data = {}
        for item in agrupacion:
            homologado_nombre = item['homologado__nombre']
            bodega_nombre = item['bodega__nombre']

            if homologado_nombre not in data:
                data[homologado_nombre] = []

            bodega_data = {
                'bodega': bodega_nombre,
                'estados': {
                    'Nuevo': item['nuevo_count'],
                    'Usado': item['usado_count'],
                    'Dañado': item['danado_count'],
                    'Revisar': item['revisar_count'],
                }
            }

            data[homologado_nombre].append(bodega_data)

        # Convert the data dict to a list to ensure JSON compatibility
        result = [{'homologado': k, 'bodegas': v} for k, v in data.items()]

        return Response(result)




class GetEquipoInstalado_EquipoView(APIView):
    def get(self, request, equipo_id):
        try:
            equipos_instalados = EquipoInstalado.objects.filter(equipo__id=equipo_id)
            serializer = EquipoInstaladoSerializer(equipos_instalados, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except EquipoInstalado.DoesNotExist:
            return Response({"error": "Equipo no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        
        
class GetEquipoBodega_EquipoView(APIView):
    def get(self, request, equipo_id):
        try:
            equipo_bodega = EquipoMovimientoBodega.objects.filter(equipo__id=equipo_id)
            serializer = EquipoMovimientoBodegaSerializer(equipo_bodega, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except EquipoMovimientoBodega.DoesNotExist:
            return Response({"error": "Equipo no encontrado"}, status=status.HTTP_404_NOT_FOUND)

class InventarioPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 2000


class GetEquipoInstaldo_AllFilter(generics.ListAPIView):
   queryset = EquipoInstalado.objects.all().order_by('-id')
   serializer_class = EquipoInstaladoSerializer
   filter_backends = [DjangoFilterBackend]
   pagination_class = InventarioPagination
   filterset_class = EquiposInstaladoFilter
    