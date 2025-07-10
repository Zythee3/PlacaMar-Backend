from django.urls import path
from .views import PlacaListAPIView

urlpatterns = [
    path('', PlacaListAPIView.as_view(), name='lista-placas'),
]
