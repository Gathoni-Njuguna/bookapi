from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import RegisterView
from rest_framework.authtoken.views import obtain_auth_token
router = DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'reviews', views.ReviewViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    
]