from django.urls import path, include
from rest_framework.routers import DefaultRouter, SimpleRouter

from library_app.api.views import (
    LibraryApiViewSet,
)

router = DefaultRouter()
router.register('libraries', LibraryApiViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
