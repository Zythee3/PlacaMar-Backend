from django.urls import path, include
from . import views

urlpatterns = [
    path('placas/', include('api.placas.urls')),
    path('choices/', views.get_choices_view, name='choices'),
    path('cidades-por-estado/<int:estado_id>/', views.get_cidades_por_estado_view, name='cidades_por_estado'),
]
