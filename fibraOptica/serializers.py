from rest_framework import serializers
from .modelsTrazos import Trazo1, Trazo2, Trazo3
from .modelsCuartoEquipos import OLT, TarjetaOLT, PuertoTarjeta
from .modelsCuartoEquipos import ODF, PuertoODF, TrazoPachcord


class OLTSerializer(serializers.ModelSerializer):
    #value = serializers.CharField(source='id', read_only=True)
    #label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = OLT
        fields = '__all__'
        
class TarjetaOLTSerializer(serializers.ModelSerializer):
    #value = serializers.CharField(source='id', read_only=True)
    #label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = TarjetaOLT
        fields = '__all__'
        
        
        
class Trazo3Serializer(serializers.ModelSerializer):
    mufa_trazo3 = serializers.CharField(source='lleg_Mufa.nombre', allow_null=True)
    caja_nap_trazo3 = serializers.CharField(source='lleg_Caja.nombreNap', allow_null=True)
    hilo_trazado_trazo3 = serializers.CharField(source='hiloTrazado.nombre', allow_null=True)
    hilo_salida_trazo3 = serializers.CharField(source='hiloSalida.nombre', allow_null=True)

    class Meta:
        model = Trazo3
        fields = '__all__'
        
        
class Trazo2Serializer(serializers.ModelSerializer):
    trazo3= Trazo3Serializer(many=True,read_only=True,allow_null=True )
    class Meta:
        model = Trazo2
        fields = "__all__"
        
       
class Trazo1FSerializer(serializers.ModelSerializer):
    trazo2= Trazo2Serializer(many=True,read_only=True )
    hiloTrazo1name= serializers.CharField(source='hiloTrazado.nombre',allow_null=True)
    #value = serializers.CharField(source='id', read_only=True)
    #label = serializers.CharField(source='puerto', read_only=True)
    class Meta:
        model = Trazo1
        fields = '__all__'    
        
class TrazoPachcordSerializer(serializers.ModelSerializer):
    trazo1= Trazo1FSerializer(many=True,read_only=True )
    class Meta:
        model = TrazoPachcord
        fields = '__all__'

class PuertoTarjetaSerializer(serializers.ModelSerializer):
    patchcors= TrazoPachcordSerializer(many=True,read_only=True )
    #value = serializers.CharField(source='id', read_only=True)
    #label = serializers.CharField(source='puerto', read_only=True)
    class Meta:
        model = PuertoTarjeta
        fields = '__all__'
        
class ODFSerializer(serializers.ModelSerializer):
    #value = serializers.CharField(source='id', read_only=True)
    #label = serializers.CharField(source='nombre', read_only=True)
    class Meta:
        model = ODF
        fields = '__all__'

class PuertoODFSerializer(serializers.ModelSerializer):
    #value = serializers.CharField(source='id', read_only=True)
    #label = serializers.CharField(source='puerto', read_only=True)
    class Meta:
        model = PuertoODF
        fields = '__all__'
        
 

        #########


# class Trazo2Serializer(serializers.ModelSerializer):
#     olt = serializers.CharField(source='sal_trazo1.sal_trazoPatchcord.sal_puertoTarjeta.tarjeta.olt.nombre')
#     tarjeta_olt = serializers.CharField(source='sal_trazo1.sal_trazoPatchcord.sal_puertoTarjeta.tarjeta.nombre')
#     puerto_tarjeta = serializers.CharField(source='sal_trazo1.sal_trazoPatchcord.sal_puertoTarjeta.puerto')
#     puerto_odf = serializers.IntegerField(source='sal_trazo1.sal_trazoPatchcord.lleg_puertoODF.puerto')
#     mufa_trazo1 = serializers.CharField(source='sal_trazo1.lleg_Mufa.nombre', allow_null=True)
#     caja_nap_trazo1 = serializers.CharField(source='sal_trazo1.lleg_Caja.nombreNap', allow_null=True)
#     hilo_trazado_trazo1 = serializers.CharField(source='sal_trazo1.hiloTrazado.nombre', allow_null=True)
#     hilo_salida_trazo1 = serializers.CharField(source='sal_trazo1.hiloSalida.nombre', allow_null=True)
#     mufa_trazo2 = serializers.CharField(source='lleg_Mufa.nombre', allow_null=True)
#     caja_nap_trazo2 = serializers.CharField(source='lleg_Caja.nombreNap', allow_null=True)
#     hilo_trazado_trazo2 = serializers.CharField(source='hiloTrazado.nombre', allow_null=True)
#     hilo_salida_trazo2 = serializers.CharField(source='hiloSalida.nombre', allow_null=True)
#     trazo3 = Trazo3Serializer(source='trazo3_set', many=True, required=False)

#     class Meta:
#         model = Trazo2
#         fields = "__all__"
        
        
        

        
     