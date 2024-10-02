from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TipoClienteViewSet,NacionalidadClienteViewSet,CiudadViewSet
from .views import BarrioViewSet, ComunidadViewSet, ClienteViewSet,ViviendaViewSet,ClienteViviendaViewSet
from .views import GetBarrio_ciudad, GetComunidad_ciudad
from .views import OrdenInstalacionViewSet, GetOrdenes_estado
from .views import GetClienteVivienda_cliente, PlanClienteViviendaViewSet, OrdenCobroViewSet
from .views import PlanViewSet, GetPlan_ClienteVivienda_clienteVivienda, UpgradeViewSet

from .views2 import ClienteListFilterView,GetOrdenCobro_clienteVivienda_sinPagar
from .views2 import GetPagosPlanClienteVivienda_View, PagosPlanClienteViviendaViewSet, getOrdenesPagadas_planClienteVivienda
from .views2 import generar_ordenes_cobro_view

from .viewsMantenimiento import QuejaCliente_crud,DiagnosticoPreliminar_crud,DiagnosticoInSitu_crud
from .viewsMantenimiento import SolucionQuejaCliente_crud, Mantenimiento_crud, SolicitudesCliente_crud
from .viewsMantenimiento import RespuestaSolicitudesCliente_crud, AtencionSolicitudesCliente_crud

router = DefaultRouter()
##MANTENIMIENTO
router.register(r'queja_cliente', QuejaCliente_crud)
router.register(r'queja_cliente_diagnostico_preliminar', DiagnosticoPreliminar_crud)
router.register(r'queja_cliente_diagnostico_in_situ', DiagnosticoInSitu_crud)
router.register(r'queja_cliente_solucion_queja', SolucionQuejaCliente_crud)
router.register(r'queja_cliente_mantenimiento', Mantenimiento_crud)
router.register(r'solicitudes_cliente', SolicitudesCliente_crud)
router.register(r'solicitudes_cliente_respuestas', RespuestaSolicitudesCliente_crud)
router.register(r'solicitudes_cliente_atencion', AtencionSolicitudesCliente_crud)

####


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
router.register(r'orden_cobro', OrdenCobroViewSet)
router.register(r'plan_internet', PlanViewSet)
router.register(r'upgrade', UpgradeViewSet)

router.register(r'pagosplan_clientevivienda', PagosPlanClienteViviendaViewSet)


#router.register(r'diversificaciones', DiversificacionViewSet)
#router.register(r'retiros', RetiroViewSet)

urlpatterns = [
    path('', include(router.urls)),
    
    path('barrio_ciudad/', GetBarrio_ciudad.as_view(),),
    path('comunidad_ciudad/', GetComunidad_ciudad.as_view(),),
    path('ordenes_estado/', GetOrdenes_estado.as_view(),),
    path('cliente_vivienda_cliente/', GetClienteVivienda_cliente.as_view(),),
    path('plan_clientevivienda_clientevivienda/', GetPlan_ClienteVivienda_clienteVivienda.as_view(),),
    
    path('orden_cobro_cliente_sin_pagar/', GetOrdenCobro_clienteVivienda_sinPagar.as_view(),),
    path('get_ordenes_pagadas_plancliente/<int:id>/', getOrdenesPagadas_planClienteVivienda),
    path('cliente_filter/', ClienteListFilterView.as_view(),),
    path('get_pagos_plan_cliente_vivienda/', GetPagosPlanClienteVivienda_View.as_view(),),
    
    ## ojo solo para ordenes de cobro
    path('generar-ordenes-cobro/<str:fecha>/', generar_ordenes_cobro_view, name='generar_ordenes_cobro'),
    
    
]