from django.urls import path, include

urlpatterns = [
    path('placas/', include('api.placas.urls')), 
]
