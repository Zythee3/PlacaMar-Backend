from django.urls import path
from .views import AdminCreateView, AdminViewSet, RegistrarLocalizacaoView, MeuRoteiroView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'admins', AdminViewSet, basename='admin')

urlpatterns = [
    path('cadastro/', AdminCreateView.as_view(), name='admin-cadastro'),
    path('registrar-localizacao/', RegistrarLocalizacaoView.as_view(), name='registrar-localizacao'),
    path('meu-roteiro/', MeuRoteiroView.as_view(), name='meu-roteiro'),
] + router.urls
