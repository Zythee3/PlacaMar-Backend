from django.urls import path
from .views import UsuarioCreateView

urlpatterns = [
    path('cadastro/', UsuarioCreateView.as_view(), name='usuario-cadastro'),
]
