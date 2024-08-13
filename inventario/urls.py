from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TipoEquipoViewSet,HomologadoViewSet,BodegaViewSet
from .views import EquipoViewSet,EquipoMovimientoBodegaViewSet
from .views import EquipoInstaladoViewSet, GetEquipoInstaladoActivo_Plan
from .views import ListaEquipo_NoInstalatoViewSet

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
  
]
