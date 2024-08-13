from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TipoClienteViewSet,NacionalidadClienteViewSet,CiudadViewSet
from .views import BarrioViewSet, ComunidadViewSet, ClienteViewSet,ViviendaViewSet,ClienteViviendaViewSet
from .views import GetBarrio_ciudad, GetComunidad_ciudad
from .views import OrdenInstalacionViewSet, GetOrdenes_estado
from .views import GetClienteVivienda_cliente, PlanClienteViviendaViewSet
from .views import PlanViewSet, GetPlan_ClienteVivienda_clienteVivienda, UpgradeViewSet


router = DefaultRouter()
router.register(r'tipo', TipoClienteViewSet)
router.register(r'nacionalidad', NacionalidadClienteViewSet)
router.register(r'ciudad', CiudadViewSet)
router.register(r'barrio', BarrioViewSet)
router.register(r'comunidad', ComunidadViewSet)
router.register(r'cliente', ClienteViewSet)
router.register(r'vivienda', ViviendaViewSet)
router.register(r'clientevivienda', ClienteViviendaViewSet)
router.register(r'ordeninstalacion', OrdenInstalacionViewSet)
router.register(r'plan_clientevivienda', PlanClienteViviendaViewSet)
router.register(r'plan_internet', PlanViewSet)
router.register(r'upgrade', UpgradeViewSet)
#router.register(r'diversificaciones', DiversificacionViewSet)
#router.register(r'retiros', RetiroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    path('barrio_ciudad/', GetBarrio_ciudad.as_view(),),
    path('comunidad_ciudad/', GetComunidad_ciudad.as_view(),),
    path('ordenes_estado/', GetOrdenes_estado.as_view(),),
    path('cliente_vivienda_cliente/', GetClienteVivienda_cliente.as_view(),),
    path('plan_clientevivienda_clientevivienda/', GetPlan_ClienteVivienda_clienteVivienda.as_view(),),
]
