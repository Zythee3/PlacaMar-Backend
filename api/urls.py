from django.urls import path
from .views import geojson_placas_view

urlpatterns = [
    path('placas/', geojson_placas_view),
]
