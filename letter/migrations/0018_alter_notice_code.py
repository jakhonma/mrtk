# Generated by Django 5.0.7 on 2024-11-21 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0017_alter_notice_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='code',
            field=models.PositiveBigIntegerField(default=5212991640, unique=True),
        ),
    ]