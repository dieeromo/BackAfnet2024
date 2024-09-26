import django_filters
from .models import Mikrotik_PlanClienteVivienda
from django.db.models import Q

class Mikrotik_PlanClienteVivienda_Filter(django_filters.FilterSet):
    planCliente = django_filters.CharFilter(field_name='planCliente')
    class Meta:
        model = Mikrotik_PlanClienteVivienda
        fields = ['planCliente', ]


