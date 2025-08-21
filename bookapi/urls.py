# bookapi/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from rest_framework.authtoken import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,)
from api.views import RegisterView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', views.obtain_auth_token),
    
    # Redirect /books/ to /api/books/
    path('books/', RedirectView.as_view(url='/api/books/', permanent=False)),
    
    # Optional: Redirect root to API documentation or books list
    path('', RedirectView.as_view(url='/api/books/', permanent=False)),
   path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]