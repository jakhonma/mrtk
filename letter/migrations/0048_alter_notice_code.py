# Generated by Django 5.1.3 on 2024-12-19 04:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0047_alter_notice_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='code',
            field=models.PositiveBigIntegerField(default=17121097730677, unique=True),
        ),
    ]
