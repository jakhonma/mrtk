from django_filters import rest_framework as filters
from .models import Information


class InformationFilter(filters.FilterSet):
    fond = filters.BaseInFilter(field_name='fond__id', lookup_expr='in')
    fond__department__name = filters.CharFilter(field_name='fond__department__name', lookup_expr='icontains')

    class Meta:
        model = Information
        fields = ['fond__department__name', 'fond']
