from django.urls import path, include
from django.contrib import admin
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', admin.site.urls),  # Rota raiz para o admin do Django
    path('admin/', admin.site.urls),
    path('api/admin/', include('core_admin.urls')),
    path('api/usuarios/', include('usuarios.urls')),
    path('api/placas/', include('api.placas.urls')),

    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),
]
