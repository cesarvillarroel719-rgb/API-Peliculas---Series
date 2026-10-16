from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PeliculaViewSet, SerieViewSet, bienvenida

# Configuración del Router para los endpoints REST
router = DefaultRouter()
router.register(r'peliculas', PeliculaViewSet)
router.register(r'series', SerieViewSet)

urlpatterns = [
    path('', bienvenida, name='bienvenida'),         # Página principal HTML
    path('api/', include(router.urls)),              # Los endpoints CRUD (ej. /api/peliculas/)
]