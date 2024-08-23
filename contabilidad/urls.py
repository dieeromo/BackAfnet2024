from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsFacturasProveedores import CajaViewSet,ProveedorEquipoViewSet,ModoCompraViewSet
from .viewsFacturasProveedores import ModoPagoProveedorViewSet,PresupuestoViewSet
from .viewsFacturasProveedores import FacturaEquipoViewSet,PagoFacturaEquipoViewSet
from .viewsFacturasProveedores import Get_FacturaEquip_View

router = DefaultRouter()
router.register(r'caja', CajaViewSet)
router.register(r'proveedor_equipo',ProveedorEquipoViewSet )
router.register(r'modo_compra', ModoCompraViewSet)
router.register(r'modo_pago',ModoPagoProveedorViewSet )
router.register(r'presupuesto',PresupuestoViewSet )
router.register(r'factura_equipo',FacturaEquipoViewSet )
router.register(r'pago_factura_equipo',PagoFacturaEquipoViewSet )


urlpatterns = [
    path('', include(router.urls)),
    path('factura_equipo_search/', Get_FacturaEquip_View.as_view(),),
    
  
]
