# Generated by Django 5.1.3 on 2024-12-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0040_alter_information_brief_data_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='single_code',
            field=models.PositiveBigIntegerField(default=16963606490862, editable=False),
        ),
    ]