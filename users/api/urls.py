from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from users.api.views import (
    UserApiViewSet,
    UserLoginView,
    LibrarianViewSet,
    CustomerViewSet,
)

router = DefaultRouter()
router.register('users', UserApiViewSet)
router.register('librarians', LibrarianViewSet)
router.register('customers', CustomerViewSet)

librarian_urls = [

]

customer_urls = [

]

urlpatterns = [
    path('', include(router.urls)),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', UserLoginView.as_view(), name='login'),
]

urlpatterns += librarian_urls + customer_urls
