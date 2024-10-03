import django_filters
from .models import OrdenCobro
from django.db.models import Q
from django_filters import DateFromToRangeFilter


class OrdenCobroFilter(django_filters.FilterSet):
    cliente = django_filters.CharFilter(field_name='planClienteVivienda__clienteVivienda__cliente__nombresApellidos', lookup_expr='icontains')
    mes_pago_servicio = DateFromToRangeFilter(field_name='mes_pago_servicio')
    plan = django_filters.CharFilter(field_name='plan__nombre', lookup_expr='icontains')
    estadoPlanCliente = django_filters.CharFilter(field_name='planClienteVivienda__estado', lookup_expr='icontains')
    subEstadoPlanCliente = django_filters.CharFilter(field_name='planClienteVivienda__estadoServicio', lookup_expr='icontains')
    estadoOrden = django_filters.CharFilter(field_name='estado', lookup_expr='icontains')
    class Meta:
        model = OrdenCobro
        fields = ['cliente', 'mes_pago_servicio','plan','estadoPlanCliente','subEstadoPlanCliente','estadoOrden']
        
