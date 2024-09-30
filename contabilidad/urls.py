from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .viewsFacturasProveedores import CajaViewSet,ProveedorEquipoViewSet,ModoCompraViewSet
from .viewsFacturasProveedores import ModoPagoProveedorViewSet,PresupuestoViewSet
from .viewsFacturasProveedores import FacturaEquipoViewSet,PagoFacturaEquipoViewSet
from .viewsFacturasProveedores import Get_FacturaEquip_View
## vistas de facturas servicio
from .viewsFacturaServicio import Servicio_crud
from .viewsFacturaServicio import FacturaServicio_crud,PagoFacturaServicio_crud
from .viewsFacturaServicio import FacturaServicio_Filter,PagoFacturaServicio_Filter
## vistas de factura varioas
from .viewsFacturaVarios import Varios_crud
from .viewsFacturaVarios import FacturaVarios_crud, PagoFacturaVarios_crud
from . viewsFacturaVarios import FacturaVarios_Filter, PagoFacturaVarios_Filter

router = DefaultRouter()
router.register(r'caja', CajaViewSet)  
router.register(r'proveedor_equipo',ProveedorEquipoViewSet )
router.register(r'modo_compra', ModoCompraViewSet)
router.register(r'modo_pago',ModoPagoProveedorViewSet )
router.register(r'presupuesto',PresupuestoViewSet )
router.register(r'factura_equipo',FacturaEquipoViewSet )
router.register(r'pago_factura_equipo',PagoFacturaEquipoViewSet )
######## crud de facturas servicios
router.register(r'servicio',Servicio_crud )
router.register(r'factura_servicio',FacturaServicio_crud)
router.register(r'pago_factura_servicio',PagoFacturaServicio_crud )

## crud de factura varios
router.register(r'varios',Varios_crud)
router.register(r'factura_varios',FacturaVarios_crud)
router.register(r'pago_factura_varios',PagoFacturaVarios_crud )



urlpatterns = [
    path('', include(router.urls)),
    path('factura_equipo_search/', Get_FacturaEquip_View.as_view(),),
    # factura servicio
    
    
    path('factura_servicio_filter/', FacturaServicio_Filter.as_view(),),
    #EJMPLO http://localhost:8003/contabilidad/factura_servicio_filter/?page=1&servicio=net&proveedor=a&fecha_emision_after=2024-12-01&fecha_emision_before=2024-12-31
  # Se filtra las facturas el 1ro de dic de 2024 y 31 dic de 2024
  
    path('pago_factura_servicio_filter/', PagoFacturaServicio_Filter.as_view(),),
  #http://localhost:8003/contabilidad/pago_factura_servicio_filter/?page=1&facturaServicios=inter&fecha_pago_after=2023-12-12&fecha_pago_before=2024-12-31
  #fecha desde el 12 dic de 2023 hasta 31 dic 2024
  
  
  path('factura_varios_filter/', FacturaVarios_Filter.as_view(),),
  #http://localhost:8003/contabilidad/factura_varios_filter/?page=1&vario=refri&descripcion=re&fecha_emision_after=2024-09-01&fecha_emision_before=2024-09-30

  
  path('pago_factura_varios_filter/', PagoFacturaVarios_Filter.as_view(),),
  #http://localhost:8003/contabilidad/pago_factura_varios_filter/?page=1&numerofacturaVarios=001&caja=di&fecha_pago_after=2024-12-12&fecha_pago_before=2024-12-31
]
