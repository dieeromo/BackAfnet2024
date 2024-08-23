from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TipoEquipoViewSet,HomologadoViewSet,BodegaViewSet
from .views import EquipoViewSet,EquipoMovimientoBodegaViewSet
from .views import EquipoInstaladoViewSet, GetEquipoInstaladoActivo_Plan
from .views import ListaEquipo_NoInstalatoViewSet
from .viewEquipos import GetEquipoListFilter_View
from .viewEquipos import EquipoCountView, EquipoCount_bodega_View
from .viewEquipos import GetEquipoInstalado_EquipoView, GetEquipoBodega_EquipoView
router = DefaultRouter()
router.register(r'tipo_equipo', TipoEquipoViewSet)
router.register(r'homologado',HomologadoViewSet )
router.register(r'bodega', BodegaViewSet)
router.register(r'equipo', EquipoViewSet)
router.register(r'equipo_moviiento_bodega',EquipoMovimientoBodegaViewSet )
router.register(r'equipo_instalado',EquipoInstaladoViewSet )
router.register(r'lista_equipo_noinstalado',ListaEquipo_NoInstalatoViewSet )

urlpatterns = [
    path('', include(router.urls)),
    path('equipo_instalado_activo_plan/', GetEquipoInstaladoActivo_Plan.as_view(),),
    path('get_equipos_filter/', GetEquipoListFilter_View.as_view()),
  #  path('estadistica-equipos/', EstadisticaEquipos_View.as_view()),
  #  path('estadistica-equipos-general/', EstadisticaEquiposGeneral_View.as_view()),
    
    
    path('estadistica-filtro/', EquipoCountView.as_view()),
    path('estadistica-filtro-bodega/', EquipoCount_bodega_View.as_view()),
    
    path('equiposInstalado_equipo/<int:equipo_id>/', GetEquipoInstalado_EquipoView.as_view()),
    path('equiposBodega_equipo/<int:equipo_id>/', GetEquipoBodega_EquipoView.as_view()),  
]
