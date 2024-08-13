from django.contrib import admin
from .models import TipoInstitucion, Institucion, Inversion, Destino, Diversificacion
from .models import SubDestino, Retiro


admin.site.register(TipoInstitucion)
admin.site.register(Institucion)
admin.site.register(Inversion)
admin.site.register(Destino)
admin.site.register(Diversificacion)
admin.site.register(SubDestino)
admin.site.register(Retiro)