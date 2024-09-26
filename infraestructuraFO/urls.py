from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MufaViewSet, CajaNapViewSet
from .views import MufaListFilter_View, PuertoTarjetaOLTViewSet

router = DefaultRouter()
router.register(r'mufa_crud', MufaViewSet)
router.register(r'cajanap_crud', CajaNapViewSet)
router.register(r'puerto_tarjeta_crud', PuertoTarjetaOLTViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('mufa_list_filter/', MufaListFilter_View.as_view(),),

]
