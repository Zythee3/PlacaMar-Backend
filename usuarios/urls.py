from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioCreateView, UsuarioViewSet

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('cadastro/', UsuarioCreateView.as_view(), name='usuario-cadastro'),
    path('', include(router.urls)),
]