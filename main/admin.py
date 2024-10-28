from django.contrib import admin
from .models import Information, Poster, Cadre

admin.site.register([Information, Poster, Cadre])
# @admin.register(Information)
# class InformationAdmin(admin.ModelAdmin):
#     search_fields = ['id', 'name']
