from django.contrib import admin

from .models import TipoEquipo, Homologado, Bodega, Equipo, EquipoMovimientoBodega
from .models import EquipoInstalado

admin.site.register(TipoEquipo)
admin.site.register(Homologado)
admin.site.register(Bodega)
admin.site.register(Equipo)
admin.site.register(EquipoMovimientoBodega)
admin.site.register(EquipoInstalado)