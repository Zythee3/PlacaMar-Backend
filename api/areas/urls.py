from django.urls import path
from .views import AreaList

urlpatterns = [
    path('', AreaList.as_view(), name='area-list'),
]
