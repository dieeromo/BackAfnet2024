import django_filters
from .models import FacturasVarios, PagoFacturasVarios
from django.db.models import Q
from django_filters import DateFromToRangeFilter


class FacturaVariosFilter(django_filters.FilterSet):
    vario = django_filters.CharFilter(field_name='vario__nombre', lookup_expr='icontains')
    descripcion = django_filters.CharFilter(field_name='descripcion', lookup_expr='icontains')
    fecha_emision = DateFromToRangeFilter(field_name='fecha_emision')
    class Meta:
        model = FacturasVarios
        fields = ['vario', 'descripcion','fecha_emision']
        


class PagoFacturaServicioFilter(django_filters.FilterSet):
    numerofacturaVarios = django_filters.CharFilter(field_name='facturaVarios__numeroFactura', lookup_expr='icontains')
    caja= django_filters.CharFilter(field_name='caja__nombre', lookup_expr='icontains')
    fecha_pago = DateFromToRangeFilter(field_name='fecha_pago')
  
    class Meta:
        model = PagoFacturasVarios
        fields = ['numerofacturaVarios','caja', 'fecha_pago']
    