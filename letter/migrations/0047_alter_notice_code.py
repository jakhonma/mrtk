# Generated by Django 5.1.3 on 2024-12-16 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('letter', '0046_alter_notice_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notice',
            name='code',
            field=models.PositiveBigIntegerField(default=26801084694344, unique=True),
        ),
    ]
