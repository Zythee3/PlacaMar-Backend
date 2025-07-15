from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlacaViewSet

router = DefaultRouter()
router.register(r'', PlacaViewSet, basename='placa')

urlpatterns = [
    path('', include(router.urls)),
]
