from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import conectar_mikrotik, firewall_cortar
from .views2 import cortar_usuario, habilitar_usuario

from .views3 import RouterMK_Crud_View, AP_nodos_Crud_View,Mikrotik_PlanClienteVivienda_Crud_View
from .views3 import Mikrotik_PlanCliente_View
from .views3 import ClientesConectadosCajaNapView, ClientesConectados_AP_View, AP_nodos_FilterViewSet
router = DefaultRouter()
router.register(r'RouterMK_Crud_View', RouterMK_Crud_View)
router.register(r'AP_nodos_Crud_View', AP_nodos_Crud_View)
router.register(r'Mikrotik_PlanClienteVivienda_Crud_View', Mikrotik_PlanClienteVivienda_Crud_View)
router.register(r'ap_nodos_filter', AP_nodos_FilterViewSet)
urlpatterns = [
    path('', include(router.urls)),

    path('conectar/', conectar_mikrotik,),
    path('cortar/', firewall_cortar,),
    path('cortar_usuario/', cortar_usuario,),
    path('habilitar_usuario/', habilitar_usuario,),
    
    path('mikrotikPlanCliente/',Mikrotik_PlanCliente_View.as_view(),),
    
    path('cajanap/clientes/<int:caja_nap_id>/', ClientesConectadosCajaNapView.as_view(), ),
    path('ap/clientes/<int:ap_id>/', ClientesConectados_AP_View.as_view(), ),
  
]
