# Generated by Django 5.1.3 on 2024-12-13 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0037_alter_notice_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='code',
            field=models.PositiveBigIntegerField(default=10723487803291, unique=True),
        ),
    ]
