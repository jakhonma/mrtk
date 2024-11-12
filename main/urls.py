from django.urls import path, include
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register("information", views.InformationViewSet)
router.register("cadre", views.CadreViewSet)

urlpatterns = [
    # Information
    path('', include(router.urls)),
    path('information/<int:information_id>/serials/', views.SerialAPIView.as_view()),
    path('information/<int:information_id>/serial/', views.SerialAPIView.as_view()),
    path('information/<int:information_id>/serial/<int:pk>/', views.SerialAPIView.as_view()),
    path('create-information/', views.InformationCreateAPIView.as_view()),
    path('edit-information/<int:pk>/', views.InformationUpdateAPIView.as_view()),

    # Poster
    path('information/<int:information_id>/create-poster/', views.PosterCreateAPIView.as_view()),
]
