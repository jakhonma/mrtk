# Generated by Django 5.0.7 on 2024-11-21 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_alter_information_location_on_server_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='color',
            field=models.CharField(choices=[('coloured', 'coloured'), ('white_black', 'white_black')], default='coloured', max_length=12),
        ),
        migrations.AlterField(
            model_name='information',
            name='single_code',
            field=models.PositiveBigIntegerField(default=2381271542, editable=False),
        ),
    ]