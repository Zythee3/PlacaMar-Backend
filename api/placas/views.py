from django.urls import path
from .views import PlacaListView

urlpatterns = [
    path('placas/', PlacaListView.as_view(), name='placa-list'),
]
