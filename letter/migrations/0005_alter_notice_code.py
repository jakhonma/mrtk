# Generated by Django 5.1.2 on 2024-11-07 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0004_alter_notice_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='code',
            field=models.PositiveBigIntegerField(default=1084919672, unique=True),
        ),
    ]