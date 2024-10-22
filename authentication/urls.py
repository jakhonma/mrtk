from django.urls import path, include
from rest_framework import routers
from authentication import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet, basename='users')

urlpatterns = [
    path('', include(router.urls)),
]
