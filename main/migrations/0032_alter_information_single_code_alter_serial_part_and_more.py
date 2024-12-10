# Generated by Django 5.1.3 on 2024-12-05 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0031_alter_information_single_code_alter_serial_part'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='single_code',
            field=models.PositiveBigIntegerField(default=22984537030159, editable=False),
        ),
        migrations.AlterField(
            model_name='serial',
            name='part',
            field=models.PositiveSmallIntegerField(),
        ),
        migrations.AddConstraint(
            model_name='serial',
            constraint=models.UniqueConstraint(fields=('information', 'part'), name='unique appversion'),
        ),
    ]