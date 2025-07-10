from django.urls import path
from .views import lista_placas

urlpatterns = [
    path('', lista_placas),
]
