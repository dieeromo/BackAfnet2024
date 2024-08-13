from django.contrib import admin
from .models import Caja, ProveedorEquipo, ModoCompra
from .models import ModoPagoProveedor,Presupuesto,FacturaEquipo, PagoFacturasEquipos
from .models import Servicio, FacturaServicios, PagoFacturasServicios

from .models import VariosF, FacturasVarios, PagoFacturasVarios
from .models import Vehiculos, InsumoVehiculo, FacturasVehiculos, PagoFacturasVehiculos
from .models import Colaboradores, PlanillaColaboradores, PagoPlanillaColaboradores
from .models import PlanillaComisiones, PagoPlanillaComisiones
# Register your models here.
admin.site.register(Caja)
admin.site.register(ProveedorEquipo)
admin.site.register(ModoCompra)
admin.site.register(ModoPagoProveedor)
admin.site.register(Presupuesto)
admin.site.register(FacturaEquipo)
admin.site.register(PagoFacturasEquipos)


admin.site.register(Servicio)
admin.site.register(FacturaServicios)
admin.site.register(PagoFacturasServicios)


admin.site.register(VariosF)
admin.site.register(FacturasVarios)
admin.site.register(PagoFacturasVarios)

admin.site.register(Vehiculos)
admin.site.register(InsumoVehiculo)
admin.site.register(FacturasVehiculos)
admin.site.register(PagoFacturasVehiculos)

admin.site.register(Colaboradores)
admin.site.register(PlanillaColaboradores)
admin.site.register(PagoPlanillaColaboradores)



admin.site.register(PlanillaComisiones)
admin.site.register(PagoPlanillaComisiones)

