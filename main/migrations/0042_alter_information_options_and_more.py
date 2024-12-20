# Generated by Django 5.1.3 on 2024-12-13 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_alter_information_single_code'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='information',
            options={'ordering': ['-created'], 'permissions': [('can_confidential', 'Can confidential information')]},
        ),
        migrations.AlterField(
            model_name='information',
            name='single_code',
            field=models.PositiveBigIntegerField(default=49858937778666, editable=False),
        ),
    ]