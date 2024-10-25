from django.contrib import admin
from helper.models import Fond, Department


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']


@admin.register(Fond)
class FondAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']

