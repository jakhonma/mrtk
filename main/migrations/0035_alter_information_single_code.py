# Generated by Django 5.1.3 on 2024-12-05 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0034_alter_information_single_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='single_code',
            field=models.PositiveBigIntegerField(default=35885387684973, editable=False),
        ),
    ]
