# Generated by Django 5.1.3 on 2024-12-13 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0036_alter_notice_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='code',
            field=models.PositiveBigIntegerField(default=91445825593770, unique=True),
        ),
    ]
