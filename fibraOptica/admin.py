from django.contrib import admin

from .modelsCajasMufas import Mufa, CajaNap

from .modelsCuartoEquipos import OLT,TarjetaOLT, PuertoTarjeta
from .modelsCuartoEquipos import ODF,PuertoODF,TrazoPachcord

from .modelsFibras import TipoFibra,Fibra,Ruta,Buffer,Hilo
from .modelsTrazos import Trazo1,Trazo2,Trazo3




class MufaAdmin(admin.ModelAdmin):
    list_display = ('numero','splitter', 'potencia', 'barrio','comunidad','verificado')
admin.site.register(Mufa,MufaAdmin)


class CajaNapAdmin(admin.ModelAdmin):
    list_display = ('numeroNap','mufa', 'splitter', 'puertos','potencia','verificado')
admin.site.register(CajaNap,CajaNapAdmin)


class OLTAdmin(admin.ModelAdmin):
    list_display = ('nombre','fecha_instalacion',)
admin.site.register(OLT,OLTAdmin)


class TarjetaOLTAdmin(admin.ModelAdmin):
    list_display = ('nombre','olt',)
admin.site.register(TarjetaOLT,TarjetaOLTAdmin)

class PuertoTarjetaOLTAdmin(admin.ModelAdmin):
    list_display = ('tarjeta','puerto',)
admin.site.register(PuertoTarjeta,PuertoTarjetaOLTAdmin)


class ODFAdmin(admin.ModelAdmin):
    list_display = ('nombre','fecha_instalacion',)
admin.site.register(ODF,ODFAdmin)


class PuertoODFAdmin(admin.ModelAdmin):
    list_display = ('puerto','odf',)
admin.site.register(PuertoODF,PuertoODFAdmin)

class TrazoPachcordAdmin(admin.ModelAdmin):
    list_display = ('sal_puertoTarjeta','lleg_puertoODF','verificado','comentario')
admin.site.register(TrazoPachcord,TrazoPachcordAdmin)


admin.site.register(TipoFibra)


class FibraAdmin(admin.ModelAdmin):
    list_display = ('tipoFibra','nombre','numeroBuffers','numeroHilos')
admin.site.register(Fibra,FibraAdmin)



admin.site.register(Buffer)


class RutaAdmin(admin.ModelAdmin):
    list_display = ('nombre','fibra')
admin.site.register(Ruta,RutaAdmin)

class HiloAdmin(admin.ModelAdmin):
    list_display = ('nombre','buffer','fibra')
admin.site.register(Hilo,HiloAdmin)



class trazo1Admin(admin.ModelAdmin):
    list_display = ('sal_trazoPatchcord','lleg_Mufa','lleg_Caja','hiloTrazado','hiloSalida')
admin.site.register(Trazo1,trazo1Admin)

class trazo2Admin(admin.ModelAdmin):
    list_display = ('sal_trazo1','lleg_Mufa','lleg_Caja','hiloTrazado','hiloSalida')
admin.site.register(Trazo2,trazo2Admin)

class trazo3Admin(admin.ModelAdmin):
    list_display = ('sal_trazo2','lleg_Mufa','lleg_Caja','hiloTrazado','hiloSalida')
admin.site.register(Trazo3,trazo3Admin)