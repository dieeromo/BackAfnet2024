from rest_framework import serializers
from .models import TipoCliente,NacionalidadCliente,Ciudad,Barrio,Comunidad
from .models import Cliente,Vivienda,ClienteVivienda, OrdenInstalacion
from .models import PlanClienteVivienda, Plan, Upgrade

from inventario.serializers import EquipoInstaladoSerializer

        
class TipoClienteSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = TipoCliente
        fields = '__all__'

class NacionalidadClienteSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = NacionalidadCliente
        fields = '__all__'


class BarrioSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='get_full_barrio', read_only=True)
    class Meta:
        model = Barrio
        fields = '__all__'
        
class ComunidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comunidad
        fields = '__all__'
        

class CiudadSerializer(serializers.ModelSerializer):
    barrios = BarrioSerializer(many=True,read_only=True )
    comunidades = ComunidadSerializer(many=True,read_only=True )
    class Meta:
        model = Ciudad
        fields = '__all__'
        
    

class ViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vivienda
        fields = '__all__'

class ClienteViviendaSerializer(serializers.ModelSerializer):
    cliente_name = serializers.CharField(source='cliente.nombresApellidos', read_only=True)
    digitador_name = serializers.CharField(source='digitador.first_name', read_only=True)
    vivienda_barrio = serializers.CharField(source='vivienda.barrio', read_only=True)
    vivienda_comunidad = serializers.CharField(source='vivienda.comunidad', read_only=True)
    vivienda_direccion = serializers.CharField(source='vivienda.direccion', read_only=True)
    vivienda_coordenadas = serializers.CharField(source='vivienda.coordenadas', read_only=True)
    vivienda_foto = serializers.CharField(source='vivienda.foto', read_only=True)

    
    class Meta:
        model = ClienteVivienda
        fields = '__all__'
        

class ClienteSerializer(serializers.ModelSerializer):
    clienteviviendas = ClienteViviendaSerializer(many=True,read_only=True )
    tipoClienteLabel = serializers.CharField(source='tipoCliente.nombre', read_only=True)
    nacionalidadClienteLabel = serializers.CharField(source='nacionalidadCliente.nombre', read_only=True)
    
    class Meta:
        model = Cliente
        fields = '__all__'


class OrdenInstalacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenInstalacion
        fields = '__all__'


class PlanClienteViviendaSerializer(serializers.ModelSerializer):
    planClienteViviendaID = serializers.CharField(source='id', read_only=True)
    equipoInstalado = EquipoInstaladoSerializer(many=True,read_only=True )
    class Meta:
        model = PlanClienteVivienda
        fields = '__all__'

class PlanSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = Plan
        fields = '__all__'
        
        
class UpgradeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Upgrade
        fields = '__all__'
