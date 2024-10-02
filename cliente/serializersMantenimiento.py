from rest_framework import serializers
from . modelsMantenimiento import QuejaCliente, DiagnosticoPreliminar
from . modelsMantenimiento import DiagnosticoInSitu, SolucionQuejaCliente
from . modelsMantenimiento import Mantenimiento
from . modelsMantenimiento import SolicitudesCliente,RespuestasSolicitudesCliente
from . modelsMantenimiento import AtencionSolicitudesCliente


class QuejaCliente_Serializer(serializers.ModelSerializer):
    class Meta:
        model = QuejaCliente
        fields = '__all__'
        
class DiagnosticoPreliminar_Serializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticoPreliminar
        fields = '__all__'
        
class DiagnosticoInSitu_Serializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticoInSitu
        fields = '__all__'
        
class SolucionQuejaCliente_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SolucionQuejaCliente
        fields = '__all__'
        
class Mantenimiento_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenimiento
        fields = '__all__'
        
class SolicitudesCliente_Serializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudesCliente
        fields = '__all__'

class RespuestaSolicitudesCliente_Serializer(serializers.ModelSerializer):
    class Meta:
        model = RespuestasSolicitudesCliente
        fields = '__all__'

class AtencionSolicitudesCliente_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AtencionSolicitudesCliente
        fields = '__all__'