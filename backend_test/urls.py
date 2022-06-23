from django.urls import include, path, re_path

from rest_framework.permissions import AllowAny

from .utils.healthz import healthz
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Cornershop API",
        default_version="v1",
        description="Cornershop API documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="cestrada1716@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(AllowAny,),
)

urlpatterns = [
    path("healthz", healthz, name="healthz"),
    path("cornershop_food/api/v1/", include("modules.menu.urls")),
    path("cornershop_food/api/v1/", include("modules.orders.urls")),
    path("cornershop_food/api/v1/", include("modules.users.urls")),
    path("cornershop_food/api/v1/", include("modules.dashboard.urls")),
    re_path(r'^cornershop_food/api/v1/swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^cornershop_food/api/v1/docs/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
