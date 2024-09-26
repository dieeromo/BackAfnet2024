from rest_framework import serializers
from .models import RouterMK,AP_nodos,Mikrotik_PlanClienteVivienda
from django.db.models import Count



class AP_nodosSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    routerNombre = serializers.CharField(source='router.nombre', read_only=True)
    label = serializers.SerializerMethodField()
    
  
    class Meta:
        model = AP_nodos
        fields = '__all__'
    def get_label(self, obj):
        return f'{obj.nombre} - nodo:{obj.router.nombre}'
class RouterMKSerializer(serializers.ModelSerializer):
    #apNodos = AP_nodosSerializer(many=True,read_only=True )
    router_instalado_nombre = serializers.CharField(source='router_instalado.equipo.homologado.nombre', read_only=True)
    router_instalado_serie = serializers.CharField(source='router_instalado.equipo.serie', read_only=True)
    class Meta:
        model = RouterMK
        fields = '__all__'


class Mikrotik_PlanClienteViviendaSerializer(serializers.ModelSerializer):
    inalambrico = serializers.SerializerMethodField()
    inalambricoCount = serializers.SerializerMethodField()
    fibraOptica = serializers.SerializerMethodField()
    fibraOpticaCount = serializers.SerializerMethodField()
    class Meta:
        model = Mikrotik_PlanClienteVivienda
        fields = '__all__'
    def get_inalambrico(self, obj):
        if obj.ap:
            return f'{obj.ap.nombre} - Nodo:{obj.ap.router.nombre} '
        else:
            return None
    def get_inalambricoCount(self, obj):
        if obj.ap:
            clientes_AP = Mikrotik_PlanClienteVivienda.objects.values('ap','planCliente__estado').annotate(total=Count('ap'))
            return {clientes_AP}
        else:
            return None
        
    def get_fibraOptica(self, obj):
        if obj.caja:
            
            return f'{obj.caja.nombreNap} - Mufa:{obj.caja.mufa.numero} -Puerto:{obj.caja.mufa.puerto_olt}'
        else:
            return None

    def get_fibraOpticaCount(self, obj):
        if obj.caja:
            cajaNap = Mikrotik_PlanClienteVivienda.objects.values('caja','planCliente__estado').annotate(total=Count('caja'))
            return {cajaNap}
        else:
            return None



# @api_view(['GET'])
# def EstadisticasTotaldocumentos(request):
#     estado_descriptions = {
#         0: 'Sin_subir',
#         1: 'Por_revisar',
#         2: 'Aprobado',
#         3: 'Por_corregir',
     
#     }
    
#     documentos_por_estado = DocumentoEvaluacion.objects.values('estado2').annotate(total=Count('estado2'))
    
#     # Convierte los resultados a un diccionario para la respuesta JSON
#     #estado_counts = {item['estado2']: item['total'] for item in documentos_por_estado}
#     estado_counts = {
#         estado_descriptions[item['estado2']]: item['total']
#         for item in documentos_por_estado
#     }
    
#     return Response(estado_counts)
 