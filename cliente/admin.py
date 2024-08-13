from django.contrib import admin
from .models import ClienteVivienda, ClienteViviendaHistorico, Vivienda, Plan
from .models import PlanClienteVivienda, Upgrade, Cliente, OrdenInstalacion
from .models import Ciudad, Barrio, Comunidad

# Register your models here.
admin.site.register(Cliente)
admin.site.register(OrdenInstalacion)

admin.site.register(ClienteVivienda)
admin.site.register(ClienteViviendaHistorico)
admin.site.register(Vivienda)

admin.site.register(Plan)
admin.site.register(PlanClienteVivienda)
admin.site.register(Upgrade)

admin.site.register(Ciudad)
admin.site.register(Barrio)
admin.site.register(Comunidad)
