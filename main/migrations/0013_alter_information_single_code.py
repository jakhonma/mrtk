# Generated by Django 5.1.2 on 2024-11-07 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_alter_information_single_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='single_code',
            field=models.PositiveBigIntegerField(default=2345967186, editable=False),
        ),
    ]
