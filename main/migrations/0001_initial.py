# Generated by Django 5.1.2 on 2024-10-24 07:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('helper', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Poster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='helper.category')),
                ('format', models.ManyToManyField(blank=True, related_name='format', to='helper.format')),
                ('language', models.ManyToManyField(blank=True, related_name='language', to='helper.language')),
                ('mtv', models.ManyToManyField(blank=True, related_name='mtv', to='helper.mtv')),
                ('region', models.ManyToManyField(blank=True, related_name='region', to='helper.region')),
                ('poster', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.poster')),
            ],
        ),
    ]