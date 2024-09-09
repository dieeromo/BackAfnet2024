# filters.py
import django_filters
from .modelsCajasMufas import Mufa
from django.db.models import Q



# class MufaFilter(django_filters.FilterSet):
#     barrio = django_filters.CharFilter(field_name='barrio__nombre', lookup_expr='icontains')
#     comunidad = django_filters.CharFilter(field_name='comunidad__nombre', lookup_expr='icontains')
#     ciudad = django_filters.CharFilter(method='filter_ciudad', label='Ciudad')

#     class Meta:
#         model = Mufa
#         fields = ['barrio', 'comunidad', 'ciudad']

#     def filter_ciudad(self, queryset, name, value):
#         return queryset.filter(
#             django_filters.Q(barrio__ciudad__nombre__icontains=value) |
#             django_filters.Q(comunidad__ciudad__nombre__icontains=value)
#         )
# filters.py

class MufaFilter(django_filters.FilterSet):
    barrio = django_filters.CharFilter(field_name='barrio__nombre', lookup_expr='icontains')
    comunidad = django_filters.CharFilter(field_name='comunidad__nombre', lookup_expr='icontains')
    ciudad = django_filters.CharFilter(method='filter_ciudad', label='Ciudad')

    class Meta:
        model = Mufa
        fields = ['barrio', 'comunidad', 'ciudad','numero']

    def filter_ciudad(self, queryset, name, value):
        return queryset.filter(
            Q(barrio__ciudad__nombre__icontains=value) |
            Q(comunidad__ciudad__nombre__icontains=value)
        )
