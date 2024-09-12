from rest_framework import serializers
from datetime import date, timedelta
from .models import TipoCliente,NacionalidadCliente,Ciudad,Barrio,Comunidad
from .models import Cliente,Vivienda,ClienteVivienda, OrdenInstalacion
from .models import PlanClienteVivienda, Plan, Upgrade, OrdenCobro
from .models import PagosPlanClienteVivienda, ClienteViviendaHistorico


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
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='get_full_comunidad', read_only=True)
    class Meta:
        model = Comunidad
        fields = '__all__'
        

class CiudadSerializer(serializers.ModelSerializer):
    barrios = BarrioSerializer(many=True,read_only=True )
    comunidades = ComunidadSerializer(many=True,read_only=True )
    class Meta:
        model = Ciudad
        fields = '__all__'
        
    


class ClienteViviendaSerializer(serializers.ModelSerializer):
    cliente_name = serializers.CharField(source='cliente.nombresApellidos', read_only=True)
    digitador_name = serializers.CharField(source='digitador.first_name', read_only=True)
    vivienda_barrio = serializers.CharField(source='vivienda.barrio', read_only=True)
    vivienda_comunidad = serializers.CharField(source='vivienda.comunidad', read_only=True)
    vivienda_direccion = serializers.CharField(source='vivienda.direccion', read_only=True)
    vivienda_coordenadas = serializers.CharField(source='vivienda.coordenadas', read_only=True)
    vivienda_foto = serializers.CharField(source='vivienda.foto', read_only=True)
    numero_dias = serializers.SerializerMethodField()
    class Meta:
        model = ClienteVivienda
        fields = '__all__'
    def get_numero_dias(self, obj):
        fecha_fin = obj.fecha_fin if obj.fecha_fin else date.today()
        
        if obj.fecha_inicio:
            return (fecha_fin - obj.fecha_inicio).days
        return None  # Puedes devolver 0 o cualquier otro valor si falta alguna de las fechas
        
        
class ViviendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vivienda
        fields = '__all__'

class ClienteViviendaHistoricoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClienteViviendaHistorico
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    clienteviviendas = ClienteViviendaSerializer(many=True,read_only=True )
    tipoClienteLabel = serializers.CharField(source='tipoCliente.nombre', read_only=True)
    nacionalidadClienteLabel = serializers.CharField(source='nacionalidadCliente.nombre', read_only=True)
    
    class Meta:
        model = Cliente
        fields = '__all__'
    def to_representation(self, instance):
        # Ordenar las viviendas por id antes de la serialización
        clienteviviendas = instance.clienteviviendas.order_by('-id')
        # Serializar las viviendas ordenadas
        representation = super().to_representation(instance)
        representation['clienteviviendas'] = ClienteViviendaSerializer(clienteviviendas, many=True).data
        return representation


class OrdenInstalacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrdenInstalacion
        fields = '__all__'

class UpgradeSerializer(serializers.ModelSerializer):
    planName = serializers.CharField(source='plan_upgrade.nombre', read_only=True)

    class Meta:
        model = Upgrade
        fields = '__all__'

class PlanClienteViviendaSerializer(serializers.ModelSerializer):
    planClienteViviendaID = serializers.CharField(source='id', read_only=True)
    equipoInstalado = EquipoInstaladoSerializer(many=True,read_only=True )
    upgrades = UpgradeSerializer(many=True,read_only=True )
    planValor =serializers.CharField(source='plan.valor', read_only=True)

    class Meta:
        model = PlanClienteVivienda
        fields = '__all__'


class PlanSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = Plan
        fields = '__all__'
         
class PagosPlanClienteViviendaSerializer(serializers.ModelSerializer):
    cajaName = serializers.CharField(source='caja.nombre', read_only=True)
    tipo_pago_descripcion = serializers.SerializerMethodField()
    fecha_pago_corta = serializers.SerializerMethodField()
    class Meta:
        model = PagosPlanClienteVivienda
        fields = '__all__'
        
    def get_tipo_pago_descripcion(self, obj):
        return obj.get_tipo_pago_display()
    def get_fecha_pago_corta(self, obj):
        fecha_ajustada = obj.fecha_pago - timedelta(hours=5)
        # Formato 'YYYY-MM-DD HH:MM:SS'
        return fecha_ajustada.strftime('%Y-%m-%d %H:%M:%S')
        

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
    

class OrdenCobroSerializer(serializers.ModelSerializer):
    pagosPlanClienteVivienda = PagosPlanClienteViviendaSerializer(many=True,read_only=True ) 
    mes_pago= serializers.SerializerMethodField()
    anio_pago= serializers.SerializerMethodField()
    class Meta:
        model = OrdenCobro
        fields = '__all__'
    def get_mes_pago(self, obj):
        mes = obj.mes_pago_servicio.month
        return numeroAmes(mes)
    
    def get_anio_pago(self, obj):
        anio = obj.fecha_generacion.year
        return anio
        
        
