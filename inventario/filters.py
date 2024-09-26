import django_filters
from .models import EquipoInstalado
from django.db.models import Q
from django_filters import DateFromToRangeFilter



class EquiposInstaladoFilter(django_filters.FilterSet):
    planClienteVivienda = django_filters.CharFilter(field_name='planClienteVivienda__clienteVivienda__cliente__nombresApellidos', lookup_expr='icontains')

    class Meta:
        model = EquipoInstalado
        fields = ['planClienteVivienda', ]
        
