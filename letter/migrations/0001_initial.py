# Generated by Django 5.1.2 on 2024-11-06 10:42

import django.core.validators
import django.db.models.deletion
import main.utils
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf', models.FileField(upload_to=main.utils.directory_path, validators=[django.core.validators.FileExtensionValidator(['pdf'])])),
                ('code', models.PositiveBigIntegerField(default=1571266020, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Sender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160)),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Letter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('process', models.CharField(choices=[('CREATED', 'CREATED'), ('CHANNEL_DIRECTOR', 'CHANNEL_DIRECTOR'), ('ARCHIVE_DIRECTOR', 'ARCHIVE_DIRECTOR'), ('ARCHIVE_EMPLOYEE', 'ARCHIVE_EMPLOYEE'), ('FINISHED', 'FINISHED'), ('CANCEL', 'CANCEL')], default='CREATED', max_length=18)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('notice', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='letter.notice')),
                ('sender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='letter.sender')),
            ],
        ),
    ]
