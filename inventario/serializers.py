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
    class Meta:
        model = Equipo
        fields = '__all__'
        
class EquipoMovimientoBodegaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipoMovimientoBodega
        fields = '__all__'
        
class EquipoInstaladoSerializer(serializers.ModelSerializer):
    equipoInfo = serializers.CharField(source='get_infoEquipo', read_only=True)
    class Meta:
        model = EquipoInstalado
        fields = '__all__'