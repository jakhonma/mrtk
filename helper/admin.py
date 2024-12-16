from django.contrib import admin
from helper.models import Fond, Department, Category, Mtv, Language, Region, Format


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']


@admin.register(Fond)
class FondAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['pk', 'name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['id', 'name']


admin.site.register([Mtv, Language, Region, Format])
