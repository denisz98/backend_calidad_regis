
from django.contrib import admin
from django.urls import path,include,re_path


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.user.views import Login, LogoutView, Profile

schema_view = get_schema_view(
   openapi.Info(
      title="SEA_Carrera",
      default_version='v1.0',
      description="Documentación de la API para las Carreras",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="deniszaldivarperez98@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [

   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

   path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

   path('admin/', admin.site.urls),
   # path('logout/', Logout.as_view(), name = 'logout'),
   path('login/',Login.as_view(), name = 'login'),
   path('logout/', LogoutView.as_view(), name='logout'),

   path('profile/', Profile.as_view(), name='profile'),

   path('users/', include('apps.user.api.routers')),
   path('api/', include('apps.carreras.api.urls')),

   path('variables/', include('apps.carreras.api.viewsets.variables.urls')),
   path('download/', include('apps.carreras.api.viewsets.download_files.urls')),
]
