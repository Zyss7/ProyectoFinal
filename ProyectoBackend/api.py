from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register(r'clientes', ClienteViewSet)
router.register(r'entrenadores', EntrenadorViewSet)
router.register(r'etapas', EtapaViewSet)
router.register(r'areas', AreaViewSet)
router.register(r'musculos', MusculoViewSet)
router.register(r'ejercicios', EjercicioViewSet)
router.register(r'rutina', RutinaViewSet)
router.register(r'membresias', MembresiaViewSet)

urlpatterns = router.urls
