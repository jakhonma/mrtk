# Generated by Django 5.1.3 on 2024-12-13 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0038_alter_notice_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='code',
            field=models.PositiveBigIntegerField(default=57618294995545, unique=True),
        ),
    ]
