# Generated by Django 5.1.3 on 2024-12-06 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0038_alter_information_single_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='brief_data',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='single_code',
            field=models.PositiveBigIntegerField(default=80671841755025, editable=False),
        ),
        migrations.AlterField(
            model_name='information',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]