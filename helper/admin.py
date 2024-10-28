from django.contrib import admin
from helper.models import Fond, Department, Category


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']


@admin.register(Fond)
class FondAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']
