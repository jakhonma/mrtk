# Generated by Django 5.1.2 on 2024-11-07 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0007_alter_notice_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='code',
            field=models.PositiveBigIntegerField(default=9407632539, unique=True),
        ),
    ]
