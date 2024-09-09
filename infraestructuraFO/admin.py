from django.contrib import admin

from .modelsCuarto import OLT,TarjetaOLT, PuertoTarjeta
from .modelsCajasMufas import Mufa, CajaNap
from .modelsCuarto import ODF, PuertoODF, TrazoPachcord
from .modelsTrazos import TipoFibra, CableFibra, HiloFibra,Trazo1,Trazo2,Trazo3
# Register your models here.

class MufaAdmin(admin.ModelAdmin):
    list_display = ('numero','splitter', 'splitter_adicional', 'potencia')
admin.site.register(Mufa,MufaAdmin)


class CajaNapAdmin(admin.ModelAdmin):
    list_display = ('numeroNap','mufa', 'splitter', 'splitter_adicional','potencia')
admin.site.register(CajaNap,CajaNapAdmin)

class ODFAdmin(admin.ModelAdmin):
    list_display = ('nombre','fecha_instalacion')
admin.site.register(ODF,ODFAdmin)


class PuertoODFAdmin(admin.ModelAdmin):
    list_display = ('odf','puerto')
admin.site.register(PuertoODF,PuertoODFAdmin)


class TipoFibraAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
admin.site.register(TipoFibra,TipoFibraAdmin)

class CableFibraAdmin(admin.ModelAdmin):
    list_display = ('tipoFibra','nombreRuta','numeroBuffers','numeroHilos')
admin.site.register(CableFibra,CableFibraAdmin)

class HiloFibraAdmin(admin.ModelAdmin):
    list_display = ('hilo','buffer','cableFibra')
admin.site.register(HiloFibra,HiloFibraAdmin)

class Trazo1Admin(admin.ModelAdmin):
    list_display = ('origen','hilo','mufa_destino','caja_destino')
admin.site.register(Trazo1,Trazo1Admin)

class Trazo2Admin(admin.ModelAdmin):
    list_display = ('origen','hilo','mufa_destino','caja_destino')
admin.site.register(Trazo2,Trazo2Admin)

class Trazo3Admin(admin.ModelAdmin):
    list_display = ('origen','hilo','mufa_destino','caja_destino')
admin.site.register(Trazo3,Trazo3Admin)


