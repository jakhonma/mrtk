# Generated by Django 5.1.3 on 2024-12-04 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_alter_information_single_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='single_code',
            field=models.PositiveBigIntegerField(default=17922748569623, editable=False),
        ),
    ]
