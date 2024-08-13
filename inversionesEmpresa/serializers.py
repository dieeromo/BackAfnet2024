from rest_framework import serializers
from .models import TipoInstitucion, Institucion, Inversion, Destino, Diversificacion
from .models import SubDestino, Retiro

class RetiroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retiro
        fields = '__all__'
        
class DiversificacionSerializer(serializers.ModelSerializer):
    retiros = RetiroSerializer(many=True, read_only=True)
    class Meta:
        model = Diversificacion
        fields = '__all__'

class InversionSerializer(serializers.ModelSerializer):
    diversificaciones = DiversificacionSerializer(many=True, read_only=True)
    class Meta:
        model = Inversion
        fields = '__all__'
        
class TipoInstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInstitucion
        fields = '__all__'

class InstitucionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Institucion
        fields = '__all__'

class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__'

class SubDestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubDestino
        fields = '__all__'

