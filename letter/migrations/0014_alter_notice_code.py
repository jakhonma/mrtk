# Generated by Django 5.1.2 on 2024-11-14 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0013_alter_notice_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='code',
            field=models.PositiveBigIntegerField(default=3013567967, unique=True),
        ),
    ]
