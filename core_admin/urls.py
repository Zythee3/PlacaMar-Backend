from django.urls import path
from .views import AdminCreateView, AdminViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'admins', AdminViewSet, basename='admin')

urlpatterns = [
    path('cadastro/', AdminCreateView.as_view(), name='admin-cadastro'),
] + router.urls
