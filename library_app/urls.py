from django.urls import path, include

from .views import LoginView, DashboardView, logout_request

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', logout_request, name='logout'),
    path('', DashboardView.as_view(), name='dashboard'),
]
