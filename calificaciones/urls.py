from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r"diplomados", views.DiplomadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('diplomados/create_list', views.DiplomadoCreateAndList.as_view(), name='diplomados'),
    path('estudiantes/create_list', views.EstudianteCreateAndList.as_view(), name='estudiantes'),
    path('calificaciones/create_list', views.CalificacionCreateAndList.as_view(), name='calificaciones'),
    path('modulos/create_list', views.ModuloCreateAndList.as_view(), name='modulos'),
    path('estudiantes/cantidad', views.cantidad_estudiantes),
]
