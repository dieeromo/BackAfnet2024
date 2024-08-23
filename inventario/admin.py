from django.contrib import admin

from .models import TipoEquipo, Homologado, Bodega, Equipo, EquipoMovimientoBodega
from .models import EquipoInstalado

admin.site.register(TipoEquipo)
admin.site.register(Homologado)
admin.site.register(Bodega)

admin.site.register(EquipoMovimientoBodega)


class EquipoInstaladoAdmin(admin.ModelAdmin):
    list_display = ('id','equipo', 'planClienteVivienda', 'motivo','condicion','estado','observacion')
admin.site.register(EquipoInstalado,EquipoInstaladoAdmin)


class EquipoAdmin(admin.ModelAdmin):
    list_display = ('id','homologado', 'serie', 'bodega','estado','estado2')
admin.site.register(Equipo,EquipoAdmin)