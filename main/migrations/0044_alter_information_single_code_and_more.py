# Generated by Django 5.1.3 on 2024-12-13 12:17

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0043_alter_information_single_code_bookmark'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='single_code',
            field=models.PositiveBigIntegerField(default=15399144080533, editable=False),
        ),
        migrations.AlterUniqueTogether(
            name='bookmark',
            unique_together={('user', 'information')},
        ),
    ]
