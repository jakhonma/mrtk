# Generated by Django 5.1.2 on 2024-11-06 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='fond',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='format',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='mtv',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
