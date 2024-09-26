from rest_framework import serializers
from .modelsCajasMufas import Mufa, CajaNap
from .modelsCuarto import OLT, TarjetaOLT,PuertoTarjeta,ODF,PuertoODF,TrazoPachcord
from .modelsTrazos import TipoFibra,CableFibra,HiloFibra,Trazo1,Trazo2,Trazo3


class Trazo3Serializer(serializers.ModelSerializer):

    class Meta:
        model = Trazo3
        fields = '__all__'


class Trazo2Serializer(serializers.ModelSerializer):

    class Meta:
        model = Trazo2
        fields = '__all__'


class Trazo1Serializer(serializers.ModelSerializer):

    class Meta:
        model = Trazo1
        fields = '__all__'


class HiloFibraSerializer(serializers.ModelSerializer):

    class Meta:
        model = HiloFibra
        fields = '__all__'


class CableFibraSerializer(serializers.ModelSerializer):

    class Meta:
        model = CableFibra
        fields = '__all__'


class TipoFibraSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoFibra
        fields = '__all__'


class TrazoPatchcordSerializer(serializers.ModelSerializer):

    class Meta:
        model = TrazoPachcord
        fields = '__all__'


class PuertoODFSerializer(serializers.ModelSerializer):

    class Meta:
        model = PuertoODF
        fields = '__all__'


class ODFSerializer(serializers.ModelSerializer):

    class Meta:
        model = ODF
        fields = '__all__'

class PuertoTarjetaSerializer(serializers.ModelSerializer):
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.SerializerMethodField()
  
    class Meta:
        model = PuertoTarjeta
        fields = '__all__'
    def get_label(self, obj):
        return f'{obj.tarjeta.nombre} {obj.puerto}'

class TarjetaOLTSerializer(serializers.ModelSerializer):

    class Meta:
        model = TarjetaOLT
        fields = '__all__'

class OLTSerializer(serializers.ModelSerializer):

    class Meta:
        model = OLT
        fields = '__all__'
        


class CajaNapSerializer(serializers.ModelSerializer):
    barrioName =serializers.CharField(source='barrio.nombre', read_only=True)
    comunidadName =serializers.CharField(source='comunidad.nombre', read_only=True)
    ciudadName = serializers.SerializerMethodField()
    value = serializers.CharField(source='id', read_only=True)
    label = serializers.SerializerMethodField()
    class Meta:
        model = CajaNap
        fields = '__all__'
    def get_ciudadName(self, obj):
        if obj.barrio:
            return obj.barrio.ciudad.nombre
        elif obj.comunidad:
            return obj.comunidad.ciudad.nombre
        return None
    def get_label(self, obj):
        return f'{obj.nombreNap} m:{obj.mufa.numero} p:{obj.mufa.puerto_olt.puerto}'


class MufaSerializer(serializers.ModelSerializer):
    cajasNap = CajaNapSerializer(many=True,read_only=True )
    barrioName =serializers.CharField(source='barrio.nombre', read_only=True)
    comunidadName =serializers.CharField(source='comunidad.nombre', read_only=True)
    ciudadName = serializers.SerializerMethodField()
    puertoDetalle = serializers.CharField(source='puerto_olt.tarjeta.nombre', read_only=True)
    oltDetalle = serializers.CharField(source='puerto_olt.tarjeta.olt.nombre', read_only=True)
    #ciudadName =serializers.CharField( source='comunidad.ciudad.nombre + barrio.ciudad.nombre', read_only=True)
    class Meta:
        model = Mufa
        fields = '__all__'
        
    def get_ciudadName(self, obj):
        if obj.barrio:
            return obj.barrio.ciudad.nombre
        elif obj.comunidad:
            return obj.comunidad.ciudad.nombre
        return None

