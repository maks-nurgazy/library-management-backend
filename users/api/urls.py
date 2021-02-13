from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from users.api.views import UserApiViewSet

router = SimpleRouter()
router.register('users', UserApiViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="Library User API",
        default_version='v1',
        description="Library User management endpoint documentation",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="maksnurgazy@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]