from rest_framework import serializers

from .models import TipoEquipo,Homologado,Bodega,Equipo
from .models import EquipoMovimientoBodega,EquipoInstalado

class TipoEquipoSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = TipoEquipo
        fields = '__all__'
        
class HomologadoSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = Homologado
        fields = '__all__'

class BodegaSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = Bodega
        fields = '__all__'

class EquipoSerializer(serializers.ModelSerializer):
    homologadoName = serializers.CharField(source='homologado.nombre', read_only=True)
    bodegaName = serializers.CharField(source='bodega.nombre', read_only=True)
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='get_infoEquipo', read_only=True)
    estadoDescripcion = serializers.SerializerMethodField()
    class Meta:
        model = Equipo
        fields = '__all__'
    def get_estadoDescripcion(self, obj):
        return obj.get_estado_display()
        
class EquipoMovimientoBodegaSerializer(serializers.ModelSerializer):
    equipoHomologado = serializers.CharField(source='equipo.homologado.nombre', read_only=True)
    equipoSerie = serializers.CharField(source='equipo.serie', read_only=True)
    bodegaName = serializers.CharField(source='bodega.nombre', read_only=True)
    class Meta:
        model = EquipoMovimientoBodega
        fields = '__all__'
        
class EquipoInstaladoSerializer(serializers.ModelSerializer):
    equipoInfo = serializers.CharField(source='get_infoEquipo', read_only=True)
    clienteName =serializers.CharField(source='planClienteVivienda.clienteVivienda.cliente.nombresApellidos', read_only=True)
    planName =serializers.CharField(source='planClienteVivienda.plan.nombre', read_only=True)
    direccionName =serializers.CharField(source='planClienteVivienda.clienteVivienda.vivienda.get_vivienda', read_only=True)
    diasInstalado = serializers.CharField(source='dias_instalacion', read_only=True)
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.SerializerMethodField()
    class Meta:
        model = EquipoInstalado
        fields = '__all__'
    def get_label(self, obj):
        return f'{obj.equipo.homologado.nombre} {obj.equipo.serie} {obj.planClienteVivienda.clienteVivienda.vivienda.direccion}'
