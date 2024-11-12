from django.urls import path, include
from rest_framework import routers
from helper import views

router = routers.DefaultRouter()
router.register('department', views.DepartmentViewSet)
router.register('fond', views.FondViewSet)
router.register('category', views.CategoryViewSet)
router.register('mtv', views.MTVViewSet)
router.register('format', views.FormatViewSet)
router.register('language', views.LanguageViewSet)
router.register('region', views.RegionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('category-view/', views.CategoryListView.as_view()),

    # Filter
    path('department-fond/<int:department_id>/', views.FontListDepartmentAPIView.as_view()),
    path('fond-category/<int:fond_id>/', views.CategoryFondListView.as_view()),
]
