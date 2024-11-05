from datetime import datetime

from django.contrib import admin
from .models import Information, Poster, Cadre
from import_export.admin import ImportExportModelAdmin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from main.resources import InformationAdminResource
from rangefilter import filters


@admin.register(Information)
class VideoAdmin(ImportExportModelAdmin):
    list_display = ['fond', 'category', 'sub_category', 'get_mtv', 'get_region', 'get_formats', 'name',
                    'mtv_index', 'color', 'get_duration', 'year', 'created']
    search_fields = ['name', 'mtv_index', 'year']
    autocomplete_fields = ['fond', 'category', 'sub_category', 'mtv', 'formats', 'region', 'language', 'poster']
    list_filter = [("fond", RelatedDropdownFilter), ("category", RelatedDropdownFilter),
                   ("sub_category", RelatedDropdownFilter), 'region', 'language', ('created', filters.DateRangeFilter)]
    list_select_related = ['fond', 'category', 'sub_category']
    resource_class = InformationAdminResource
    filter_horizontal = ['region']

    def get_rangefilter_created_at_default(self, request):
        return datetime.date.year, datetime.date.year

    def get_mtv(self, obj):
        return "\n".join([child.name for child in obj.mtv.all()])

    def get_region(self, obj):
        return "\n".join([child.name for child in obj.region.all()])

    def get_formats(self, obj):
        return '\n'.join([p.name for p in obj.formats.all()])

    def get_duration(self, obj):
        return f"{obj.duration}"


admin.site.register([Poster, Cadre])
