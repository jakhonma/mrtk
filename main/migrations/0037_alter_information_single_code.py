# Generated by Django 5.1.3 on 2024-12-05 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0036_alter_information_format_alter_information_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='single_code',
            field=models.PositiveBigIntegerField(default=23641161683357, editable=False),
        ),
    ]