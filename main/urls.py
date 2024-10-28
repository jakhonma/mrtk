from django.urls import path, include
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register("information", views.InformationViewSet)
router.register("cadre", views.CadreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('information/<int:information_id>/serials/', views.SerialAPIView.as_view()),
    path('information/<int:information_id>/serial/', views.SerialAPIView.as_view()),
    path('information/<int:information_id>/serial/<int:pk>/', views.SerialAPIView.as_view()),
]
