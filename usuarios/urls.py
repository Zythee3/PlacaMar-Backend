from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet, UsuarioCreateView

router = DefaultRouter()
router.register(r'', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('cadastro/', UsuarioCreateView.as_view(), name='usuario-cadastro'),
    path('', include(router.urls)),
]