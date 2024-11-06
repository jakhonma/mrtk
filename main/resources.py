from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

from authentication.models import User
from main.models import Information
from helper.models import Fond, Category, Mtv, Region, Language, Format
from typing import Any


class FondCategoryForeignKeyWidget(ForeignKeyWidget):
    def get_queryset(self, value, row, *args, **kwargs):
        fond_id = Fond.objects.get(name=row['fond'])
        return self.model.objects.filter(
            fond_id=fond_id,
            name=row["category"]
        )


class CategoryParentForeignKeyWidget(ForeignKeyWidget):
    def get_queryset(self, value, row, *args, **kwargs):
        fond = Fond.objects.get(name=row['fond'])
        category = Category.objects.get(name=row['category'], fond=fond)
        if row['parent']:
            category = Category.objects.get(name=row['parent'], parent=category)
            return self.model.objects.filter(
                parent=category,
                name=row["parent"]
            )
        else:
            return self.model.objects.filter(
                fond=fond,
                name=row["category"]
            )


class InformationAdminResource(resources.ModelResource):
    def __init__(self, user=None, *args, **kwargs):
        super().__init__()
        self.user = user

    # fond = fields.Field(
    #     column_name='fond',
    #     attribute='fond',
    #     widget=FondCategoryForeignKeyWidget(Category, field='name')
    # )
    category = fields.Field(
        column_name='category',
        attribute='category',
        widget=CategoryParentForeignKeyWidget(Category, field='name')
    )
    # category_parent = fields.Field(
    #     column_name='category',
    #     attribute='category.parent',
    #     widget=FondCategoryForeignKeyWidget(Category, field='name')
    # )
    employee = fields.Field(
        column_name='emp',
        attribute='employee',
        widget=FondCategoryForeignKeyWidget(User, field='username')
    )

    mtv = fields.Field(column_name='mtv', attribute='mtv', widget=ManyToManyWidget(Mtv, field='name'))
    region = fields.Field(column_name='region', attribute='region', widget=ManyToManyWidget(Region, field='name'))
    language = fields.Field(column_name='language', attribute='language', widget=ManyToManyWidget(Language, field='name'))
    format = fields.Field(column_name='format', attribute='format', widget=ManyToManyWidget(Format, field='name'))

    def before_import_row(self, row, **kwargs):
        self.employee = kwargs['user']
        # fond_name = row["fond"]
        # category_name = row["category"] if row["category"] is not None else None
        # sub_category_name = row["sub_category"] if row["sub_category"] is not None else None
        mtv_name = str(row["mtv"]).strip()
        region_name = str(row["region"]).strip()
        language_name = str(row["language"]).strip()
        format_name = str(row["format"]).strip()

        if "," in mtv_name:
            mtv_list = mtv_name.split(',')
            for item in mtv_list:
                Mtv.objects.get(name=item)
        elif mtv_name == 'None':
            pass
        else:
            Mtv.objects.get(name=mtv_name)

        if "," in region_name:
            region_list = region_name.split(',')
            for item in region_list:
                Region.objects.get(name=item)
            # for item in range(len(region_name)-1):
            #     if region_name[item] == ',':
            #         Region.objects.get(name=region)
            #         region = ''
            #     if count == len(region_name)-1:
            #         Region.objects.get(name=region)
            #         region = ''
            #     region += region_name[item]
            #     count +=1
        elif region_name == 'None':
            pass
        else:
            Region.objects.get(name=region_name)

        if ',' in language_name:
            lst = language_name.split(',')
            for item in lst:
                Language.objects.get(name=item)
        elif language_name == 'None':
            pass
        else:
            Language.objects.get(name=language_name)

        if ',' in format_name:
            format_list = format_name.split(',')
            for item in format_list:
                Format.objects.get(name=item)
        elif format_name == 'None':
            pass
        else:
            Format.objects.get(name=format_name)

    def save_instance(
        self, instance, is_create, using_transactions=True, dry_run=False
    ):
        instance.employee = self.employee
        super().save_instance(instance, is_create, using_transactions, dry_run)

    class Meta:
        model = Information
        fields = [
            'category', 'mtv', 'region', 'language', 'format', 'id', 'title',
            'mtv_index', 'location_on_server', 'color', 'material', 'duration',
            'year', 'month', 'day', 'restoration', 'confidential', 'brief_data',
            'summary', 'is_serial', 'part',
        ]
