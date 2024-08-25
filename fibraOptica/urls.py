
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TrazoListView, PuertoTarjetaViewSet

router = DefaultRouter()
router.register(r'puerto_tarjeta', PuertoTarjetaViewSet)

urlpatterns = [    
    path('', include(router.urls)),
    path('trazos/',TrazoListView.as_view(),),   
]
