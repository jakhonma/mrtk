from datetime import datetime
from django.contrib import admin
from main.models import Information, Poster, Cadre, Serial
from import_export.admin import ImportExportModelAdmin
from django_admin_listfilter_dropdown.filters import RelatedDropdownFilter
from main.resources import InformationAdminResource
from rangefilter import filters


@admin.register(Information)
class InformationAdmin(ImportExportModelAdmin):
    list_display = ['category', 'get_mtv', 'get_region', 'get_formats', 'title',
                    'mtv_index', 'color', 'get_duration', 'year', 'created']
    search_fields = ['name', 'mtv_index', 'year']
    # autocomplete_fields = ['category', 'mtv', 'format', 'region', 'language', 'poster']
    # list_filter = [("category", RelatedDropdownFilter), 'region', 'language', ('created', filters.DateRangeFilter)]
    # list_select_related = ['category']
    resource_class = InformationAdminResource
    filter_horizontal = ['region']

    def get_import_resource_kwargs(self, request, *args, **kwargs):
        # request.user ni ProductResource ga uzatamiz
        return {'user': request.user}

    def get_rangefilter_created_at_default(self, request):
        return datetime.date.year, datetime.date.year

    def get_mtv(self, obj):
        return "\n".join([child.name for child in obj.mtv.all()])

    def get_region(self, obj):
        return "\n".join([child.name for child in obj.region.all()])

    def get_formats(self, obj):
        return '\n'.join([p.name for p in obj.format.all()])

    def get_duration(self, obj):
        return f"{obj.duration}"


@admin.register(Serial)
class SerialAdmin(admin.ModelAdmin):
    list_display = ['id', 'part', 'duration']


admin.site.register([Poster, Cadre])
