from django.contrib import admin
from .models import ClienteVivienda, ClienteViviendaHistorico, Vivienda, Plan
from .models import PlanClienteVivienda, Upgrade, Cliente, OrdenInstalacion
from .models import Ciudad, Barrio, Comunidad
from .models import OrdenCobro, PagosPlanClienteVivienda, TipoCliente
# Register your models here.
admin.site.register(Cliente)
admin.site.register(OrdenInstalacion)
admin.site.register(Vivienda)
admin.site.register(ClienteVivienda)
admin.site.register(Ciudad)

admin.site.register(Comunidad)


admin.site.register(PagosPlanClienteVivienda)



class TipoClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
admin.site.register(TipoCliente, TipoClienteAdmin)
class BarrioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ciudad')
admin.site.register(Barrio, BarrioAdmin)
class ClienteViviendaHistoricoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'vivienda','clienteVivienda','fecha_inicio','fecha_fin')
admin.site.register(ClienteViviendaHistorico, ClienteViviendaHistoricoAdmin)


class PlanClienteViviendaAdmin(admin.ModelAdmin):
    list_display = ('id', 'clienteVivienda', 'plan','fecha_instalacion','fecha_desinstalacion','estado')
admin.site.register(PlanClienteVivienda,PlanClienteViviendaAdmin)




class UpgradeAdmin(admin.ModelAdmin):
    list_display = ('planClienteVivienda', 'plan_upgrade', 'fecha')
admin.site.register(Upgrade,UpgradeAdmin)




class PlanAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'alias', 'valor')
admin.site.register(Plan,PlanAdmin)

class OrdenCobroAdmin(admin.ModelAdmin):
    list_display = ('planClienteVivienda','plan','mes_pago_servicio','dias_consumo', 'fecha_generacion', 'fecha_vencimiento', 'valor_total','valor_subtotal','valor_iva','valor_abonado' ,'estado')
    @admin.action(description='Generar órdenes de cobro para el mes actual')
    def generar_ordenes_cobro(self, request, queryset):
        OrdenCobro.generar_ordenes_de_cobro()
        self.message_user(request, "Órdenes de cobro generadas exitosamente")

admin.site.register(OrdenCobro, OrdenCobroAdmin)