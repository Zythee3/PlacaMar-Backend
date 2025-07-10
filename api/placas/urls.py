from django.urls import path
from .views import PlacaListView

urlpatterns = [
    path('', PlacaListView.as_view(), name='lista-placas'),
]
