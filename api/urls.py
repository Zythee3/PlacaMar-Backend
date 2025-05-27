from django.urls import path
from .views import usuarios_view, dashboard_view

urlpatterns = [
    path('usuarios/', usuarios_view, name='usuarios'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
