from rest_framework import serializers
from .models import Caja,ProveedorEquipo,ModoCompra,ModoPagoProveedor
from .models import Presupuesto,FacturaEquipo,PagoFacturasEquipos
from .models import Servicio, FacturaServicios, PagoFacturasServicios
from .models import VariosF,FacturasVarios, PagoFacturasVarios
from .models import Vehiculos,InsumoVehiculo,FacturasVehiculos,PagoFacturasVehiculos
from .models import Colaboradores, PlanillaColaboradores,PagoPlanillaColaboradores
from .models import PlanillaComisiones, PagoPlanillaComisiones
        
from inventario.serializers import EquipoSerializer
class CajaSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = Caja
        fields = '__all__'
        
class ProveedorEquipoSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = ProveedorEquipo
        fields = '__all__'

class ModoCompraSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = ModoCompra
        fields = '__all__'
        
class ModoPagoProveedorSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = ModoPagoProveedor
        fields = '__all__'


class PresupuestoSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = Presupuesto
        fields = '__all__'
        
class PagoFacturaEquiposSerializer(serializers.ModelSerializer):
    cajaName=serializers.CharField(source='caja', read_only=True)
    class Meta:
        model = PagoFacturasEquipos
        fields = '__all__'


class FacturaEquipoSerializer(serializers.ModelSerializer):
    equipos = EquipoSerializer(many=True,read_only=True )
    pagosFacturaEquipos = PagoFacturaEquiposSerializer(many=True,read_only=True )
    proveedorName = serializers.CharField(source='proveedor', read_only=True)
    modoCompraName = serializers.CharField(source='modoCompra', read_only=True)
    inventarioName = serializers.CharField(source='get_inventario', read_only=True)
    equiposIngresadosName=serializers.CharField(source='get_equiposIngresados', read_only=True)
    presupuestoName=serializers.CharField(source='presupuesto', read_only=True)
    
    class Meta:
        model = FacturaEquipo
        fields = '__all__'


class ServicioSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = Servicio
        fields = '__all__'
        
        

class PagoFacturaServicioSerializer(serializers.ModelSerializer):
    numerofacturaServicio = serializers.CharField(source='facturaServicios.numeroFactura', read_only=True)
    cajaName = serializers.CharField(source='caja.nombre', read_only=True)
    modoPagoName = serializers.CharField(source='modoPago.nombre', read_only=True)
    class Meta:
        model = PagoFacturasServicios
        fields = '__all__'
        
class FacturaServicioSerializer(serializers.ModelSerializer):
    proveedorName = serializers.CharField(source='proveedor.nombre', read_only=True)
    servicioName = serializers.CharField(source='servicio.nombre', read_only=True)
    modoCompraName = serializers.CharField(source='modoCompra.nombre', read_only=True)
    presupuestoName = serializers.CharField(source='presupuesto.nombre', read_only=True)
    pagosServicios = PagoFacturaServicioSerializer(many=True,read_only=True )
    class Meta:
        model = FacturaServicios
        fields = '__all__'
        


class VariosFSerializer(serializers.ModelSerializer):
    class Meta:
        model = VariosF
        fields = '__all__'
        
        
        
class PagoFacturaVariosSerializer(serializers.ModelSerializer):
    numerofacturaVario = serializers.CharField(source='facturaVarios.numeroFactura', read_only=True)
    cajaName = serializers.CharField(source='caja.nombre', read_only=True)
    modoPagoName = serializers.CharField(source='modoPago.nombre', read_only=True)
    class Meta:
        model = PagoFacturasVarios
        fields = '__all__'
class FacturaVariosSerializer(serializers.ModelSerializer):
    varioName = serializers.CharField(source='vario.nombre', read_only=True)
    modoCompraName = serializers.CharField(source='modoCompra.nombre', read_only=True)
    presupuestoName = serializers.CharField(source='presupuesto.nombre', read_only=True)
    pagosVarios = PagoFacturaVariosSerializer(many=True,read_only=True )
    class Meta:
        model = FacturasVarios
        fields = '__all__'


        
