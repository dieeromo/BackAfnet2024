from django.contrib import admin

from .models import RouterMK, AP_nodos,Mikrotik_PlanClienteVivienda
class RouterMKAdmin(admin.ModelAdmin):
    list_display = ('nombre','router_instalado', 'ipv4_address', )
admin.site.register(RouterMK,RouterMKAdmin)


class AP_nodosAdmin(admin.ModelAdmin):
    list_display = ('nombre','ssid', 'frecuencia', 'router','ap_instalado','id')
admin.site.register(AP_nodos,AP_nodosAdmin)

class Mikrotik_Plan_Cliente_Vivienda_Admin(admin.ModelAdmin):
    list_display = ('planCliente','ap', 'caja', 'ipv4_address')
admin.site.register(Mikrotik_PlanClienteVivienda,Mikrotik_Plan_Cliente_Vivienda_Admin)
