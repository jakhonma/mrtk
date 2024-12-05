from django.urls import path, include
from rest_framework import routers
from main import views

router = routers.DefaultRouter()
router.register("information", views.InformationViewSet)
# router.register("cadre", views.CadreViewSet)

urlpatterns = [
    # Information
    path('', include(router.urls)),
    path('create-information/', views.InformationCreateAPIView.as_view()),
    path('edit-information/<int:pk>/', views.InformationUpdateAPIView.as_view()),
    path('delete-information/<int:pk>/', views.InformationDestroyAPIView.as_view()),

    # Poster
    path('information/<int:information_id>/create-poster/', views.PosterCreateAPIView.as_view()),
    path('information/<int:information_id>/delete-poster/<int:pk>/', views.PosterDeleteAPIView.as_view()),

    # Cadre
    path('information/<int:information_id>/list-cadre/', views.CadreListAPIView.as_view()), #Informationga tegishli Cadrelar list
    path('information/<int:information_id>/create-cadre/', views.CadreCreateAPIView.as_view()), #Informationga tegishli Cadrelar qo'shish
    path('information/<int:information_id>/delete-cadre/<int:pk>/', views.CadreDeleteAPIView.as_view()), #Informationga tegishli Cadrelar o'chirish

    # Serial
    path('information/<int:information_id>/list-serial/', views.SerialListAPiView.as_view()), #Informationga tegishli Seriallar listi
    path('information/<int:information_id>/one-serial/<int:pk>/', views.SerialRetrieveAPIView.as_view()), #Informationga tegishli Seriallar bittasini olish
    path('information/<int:information_id>/create-serial/', views.SerialCreateAPIView.as_view()), #Informationga tegishli Seriallar qo'shish
    path('information/<int:information_id>/edit-serial/<int:pk>/', views.SerialUpdateAPIView.as_view()), #Informationga tegishli Seriallar o'zgartirish
    path('information/<int:information_id>/delete-serial/<int:pk>/', views.SerialDestroyAPIView.as_view()), #Informationga tegishli Seriallar o'zgartirish
]
