# Generated by Django 5.1.3 on 2024-12-05 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0037_alter_information_single_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='single_code',
            field=models.PositiveBigIntegerField(default=31846428544958, editable=False),
        ),
    ]