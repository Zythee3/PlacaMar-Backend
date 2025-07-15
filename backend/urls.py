from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/usuarios/', include('api.usuarios.urls')),
    path('api/placas/', include('api.placas.urls')),
    path('api/auth/', include('rest_framework_simplejwt.urls')),
    path('api/auth/login/', TokenObtainPairView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),
]

