from django.contrib import admin
from .models import ClienteVivienda, ClienteViviendaHistorico, Vivienda, Plan
from .models import PlanClienteVivienda, Upgrade, Cliente, OrdenInstalacion
from .models import Ciudad, Barrio, Comunidad
from .models import OrdenCobro, PagosPlanClienteVivienda
# Register your models here.
admin.site.register(Cliente)
admin.site.register(OrdenInstalacion)

admin.site.register(ClienteVivienda)
admin.site.register(ClienteViviendaHistorico)
admin.site.register(Vivienda)


admin.site.register(PlanClienteVivienda)
admin.site.register(Upgrade)

admin.site.register(Ciudad)
admin.site.register(Barrio)
admin.site.register(Comunidad)

admin.site.register(PagosPlanClienteVivienda)

class PlanAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'alias', 'valor')
admin.site.register(Plan,PlanAdmin)

class OrdenCobroAdmin(admin.ModelAdmin):
    list_display = ('planClienteVivienda', 'fecha_generacion', 'fecha_vencimiento', 'valor_subtotal','valor_iva','valor_total','valor_abonado' ,'estado')
    actions = ['generar_ordenes_cobro']

    @admin.action(description='Generar órdenes de cobro para el mes actual')
    def generar_ordenes_cobro(self, request, queryset):
        OrdenCobro.generar_ordenes_de_cobro()
        self.message_user(request, "Órdenes de cobro generadas exitosamente")

admin.site.register(OrdenCobro, OrdenCobroAdmin)