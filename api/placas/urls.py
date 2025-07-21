from django.urls import path
from .views import lista_placas

urlpatterns = [
    path('placas/', lista_placas, name='lista_placas'),
]
