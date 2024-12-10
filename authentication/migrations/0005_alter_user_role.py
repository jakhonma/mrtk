# Generated by Django 5.1.3 on 2024-12-04 11:56

import utils.choices
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(blank=True, choices=utils.choices.UserRoleEnum.choices, default=utils.choices.UserRoleEnum['LOW_USER'], max_length=20),
        ),
    ]