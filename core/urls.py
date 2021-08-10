from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from artistas.api.viewsets import ArtistaViewSet, EventoArtistaViewSet
from bares.api.viewsets import BarViewSet
from bebidas.api.viewsets import BebidaViewSet
from comidas.api.viewsets import ComidaViewSet
from empresa.api.viewsets import EmpresaViewSet
from eventos.api.viewsets import EventoViewSet
from ingressos.api.viewsets import IngressoViewSet
from perfil_empresa.api.viewsets import PerfilEmpresaViewSet
from rest_framework_swagger.views import get_swagger_view
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static
from .viewset import MyTokenObtainPairView, UserViewSet

from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
router = routers.DefaultRouter()
router.register(r'artistas', ArtistaViewSet)
router.register(r'evento_artista', EventoArtistaViewSet)
router.register(r'bar', BarViewSet)
router.register(r'bebida', BebidaViewSet)
router.register(r'comida', ComidaViewSet)
router.register(r'empresa', EmpresaViewSet)
router.register(r'evento', EventoViewSet)
router.register(r'ingressos', IngressoViewSet)
router.register(r'perfil_empresa', PerfilEmpresaViewSet)
router.register(r'users', UserViewSet)


schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('api/', include(router.urls)),
    path('', include('eventos.urls')),
    path('admin/', admin.site.urls),
    path('api/token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('retorno/pagseguro/', include('pagseguro.urls')),
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

