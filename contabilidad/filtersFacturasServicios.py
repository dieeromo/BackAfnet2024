import django_filters
from .models import FacturaServicios, PagoFacturasServicios
from django.db.models import Q
from django_filters import DateFromToRangeFilter


class FacturaSericioFilter(django_filters.FilterSet):
    proveedor = django_filters.CharFilter(field_name='proveedor__nombre', lookup_expr='icontains')
    servicio = django_filters.CharFilter(field_name='servicio__nombre', lookup_expr='icontains')
    fecha_emision = DateFromToRangeFilter(field_name='fecha_emision')
    class Meta:
        model = FacturaServicios
        fields = ['proveedor', 'servicio','fecha_emision']
        


class PagoFacturaServicioFilter(django_filters.FilterSet):
    facturaServicios = django_filters.CharFilter(field_name='facturaServicios__numeroFactura', lookup_expr='icontains')
    caja= django_filters.CharFilter(field_name='caja__nombre', lookup_expr='icontains')
    fecha_pago = DateFromToRangeFilter(field_name='fecha_pago')
  
    class Meta:
        model = PagoFacturasServicios
        fields = ['facturaServicios','caja', 'fecha_pago']
    