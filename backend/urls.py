from django.http import HttpResponse
from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def home(request):
    return HttpResponse("API PlacaMar Backend funcionando!")

urlpatterns = [
    path('', home),  # Rota raiz simples
    path('admin/', admin.site.urls),
    path('api/admin/', include('core_admin.urls')),
    path('api/usuarios/', include('usuarios.urls')),
    path('api/placas/', include('api.placas.urls')),

    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),
]
