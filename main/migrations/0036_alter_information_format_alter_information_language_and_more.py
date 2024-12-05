# Generated by Django 5.1.3 on 2024-12-05 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0006_remove_category_is_child'),
        ('main', '0035_alter_information_single_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='format',
            field=models.ManyToManyField(blank=True, related_name='format', to='helper.format'),
        ),
        migrations.AlterField(
            model_name='information',
            name='language',
            field=models.ManyToManyField(blank=True, related_name='language', to='helper.language'),
        ),
        migrations.AlterField(
            model_name='information',
            name='mtv',
            field=models.ManyToManyField(blank=True, related_name='mtv', to='helper.mtv'),
        ),
        migrations.AlterField(
            model_name='information',
            name='region',
            field=models.ManyToManyField(blank=True, related_name='region', to='helper.region'),
        ),
        migrations.AlterField(
            model_name='information',
            name='single_code',
            field=models.PositiveBigIntegerField(default=32367657518404, editable=False),
        ),
    ]
