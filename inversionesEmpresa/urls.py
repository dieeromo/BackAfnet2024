# urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DiversificacionViewSet , InversionViewSet2, InversionViewSet
from .views import conectar_mikrotik

router = DefaultRouter()
router.register(r'inversiones', InversionViewSet)
router.register(r'inversiones2', InversionViewSet2)
router.register(r'diversificaciones', DiversificacionViewSet)
#router.register(r'diversificaciones', DiversificacionViewSet)
#router.register(r'retiros', RetiroViewSet)

urlpatterns = [
    path('', include(router.urls)),

     path('conectar-mikrotik/', conectar_mikrotik, name='conectar_mikrotik'),
]
