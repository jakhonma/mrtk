# Generated by Django 5.1.3 on 2024-12-14 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0043_alter_notice_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='code',
            field=models.PositiveBigIntegerField(default=15767952189699, unique=True),
        ),
    ]
