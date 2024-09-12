from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, routers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required


from django.http import JsonResponse



from .models import Cliente, OrdenCobro, PagosPlanClienteVivienda, PlanClienteVivienda
from .serializers import ClienteSerializer, OrdenCobroSerializer
from .serializers import PagosPlanClienteViviendaSerializer

class ClientePagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 2000

class ClienteListFilterView(generics.ListAPIView):
    queryset = Cliente.objects.all().order_by('-id')
    serializer_class = ClienteSerializer
    pagination_class = ClientePagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombresApellidos','cedula']  # Filtra por el nombre
    
##
    
# ORDENES DE COBROS POR CLIENTE SIN PAGAR
def numeroAmes(mes):
    nombre=''
    if mes ==1 :
        nombre='Enero'
    elif mes ==2:
        nombre='Febrero'    
    elif mes ==3:
        nombre='Marzo'
    elif mes ==4:
        nombre='Abril'
    elif mes ==5:
        nombre='Mayo'
    elif mes ==6:
        nombre='Junio'
    elif mes ==7:
        nombre='Julio'
    elif mes ==8:
        nombre='Agosto'
    elif mes ==9:
        nombre='Septiembre'
    elif mes ==10:
        nombre='Octubre'
    elif mes ==11:
        nombre='Noviembre'
    elif mes ==12:
        nombre='Diciembre'
    return nombre
    
class GetOrdenCobro_clienteVivienda_sinPagar(APIView):
    def get(self,request):
        data=[]
        planClienteVivienda_id = request.query_params.get('planclientevivienda_id', None)
        ordenes = OrdenCobro.objects.filter(planClienteVivienda=planClienteVivienda_id).exclude(estado=3)
        for ordenes_i in ordenes:
            data.append({
                'id':ordenes_i.id,
                'planClienteVivienda':ordenes_i.planClienteVivienda.plan.nombre, # OJO este cambia cada que se cambie de plan
                'valor_subtotal': ordenes_i.valor_subtotal,
                'valor_iva': round( ordenes_i.valor_iva , 2),
                'valor_total':ordenes_i.valor_total,
                'valor_abonado': ordenes_i.valor_abonado,
                'valor_pendiente': round( ordenes_i.valor_total - ordenes_i.valor_abonado, 2),
                'dias_extras':ordenes_i.dias_extras,
                'ejecucion_dias_extras':ordenes_i.ejecucion_dias_extras,
                'mes': numeroAmes( ordenes_i.mes_pago_servicio.month),
                'anio':ordenes_i.mes_pago_servicio.year,
                'dias_consumo': ordenes_i.dias_consumo,
                'plan':ordenes_i.plan.nombre, # este se mantiene fijo cuando se genero la orden
            })
        return Response(data)
    
    
######### pagos PLAN CLIENTE VIVIENDA
class PagosPlanClienteViviendaPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 2000

class GetPagosPlanClienteVivienda_View(generics.ListAPIView):
    queryset = PagosPlanClienteVivienda.objects.all()
    serializer_class = PagosPlanClienteViviendaSerializer
    pagination_class = PagosPlanClienteViviendaPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['planClienteVivienda','estado','orden_cobro','fecha_pago','caja',]  # Filtra por el nombre
    
    
class PagosPlanClienteViviendaViewSet(viewsets.ModelViewSet):
    queryset = PagosPlanClienteVivienda.objects.all()
    serializer_class = PagosPlanClienteViviendaSerializer
    router = routers.DefaultRouter()
#############
#VER PAGOS Y FACTURAS

@api_view(['GET'])
#@login_required()
def getOrdenesPagadas_planClienteVivienda(request,id):
    ordenesPagadas = OrdenCobro.objects.filter(planClienteVivienda =id).order_by('-id') 
    serializer = OrdenCobroSerializer(ordenesPagadas , many=True)
    return Response(serializer.data)







def generar_ordenes_cobro_view(request):
    OrdenCobro.generar_ordenes_de_cobro()
    return JsonResponse({"message": "Órdenes de cobro generadas exitosamente."})


# @api_view(['POST'])
# def generar_ordenes_cobro_individual_view(request):
#     data = request.data 
    
#     planClienteVivienda_id = data['planClienteVivienda_id']
#     fecha_inicio = data['fecha_inico']
#     fecha_fin = data['fecha_fin']
    
#     planCliente = PlanClienteVivienda.objects.filter(id=planClienteVivienda_id)
#     return JsonResponse({"message": "Órdenes de cobro generadas exitosamente."})
