# Generated by Django 5.1.2 on 2024-10-28 07:37

import django.db.models.deletion
import main.utils
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
                ('image', models.ImageField(blank=True, null=True, upload_to=main.utils.directory_path)),
            ],
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('mtv_index', models.CharField(max_length=100)),
                ('location_on_server', models.CharField(max_length=250)),
                ('color', models.CharField(choices=[('coloured', 'coloured'), ('write-black', 'write-black')], default='coloured', max_length=12)),
                ('material', models.CharField(choices=[('ether', 'ether'), ('primary', 'primary')], default='ether', max_length=10)),
                ('duration', models.TimeField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('single_code', models.PositiveBigIntegerField(default=1722175516, editable=False)),
                ('restoration', models.BooleanField(default=False)),
                ('confidential', models.BooleanField(default=False)),
                ('brief_data', models.TextField(blank=True, db_index=True, null=True)),
                ('summary', models.TextField(blank=True, db_index=True, null=True)),
                ('is_serial', models.BooleanField(default=False)),
                ('part', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='helper.category')),
                ('format', models.ManyToManyField(blank=True, related_name='format', to='helper.format')),
                ('language', models.ManyToManyField(blank=True, related_name='language', to='helper.language')),
                ('mtv', models.ManyToManyField(blank=True, related_name='mtv', to='helper.mtv')),
                ('region', models.ManyToManyField(blank=True, related_name='region', to='helper.region')),
                ('poster', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.poster')),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Cadre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=main.utils.directory_path)),
                ('information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='information', to='main.information')),
            ],
        ),
    ]
