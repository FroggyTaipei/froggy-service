# Generated by Django 2.1.5 on 2019-01-23 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import storages.backends.gcloud
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cases', '0002_auto_20190122_2131'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaseFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('case', '案件附件'), ('arrange', '處理紀錄附件')], default='case', max_length=20, verbose_name='File Type')),
                ('file', models.FileField(storage=storages.backends.gcloud.GoogleCloudStorage(bucket_name='froggy-service-case'), upload_to='', verbose_name='Case File')),
                ('file_name', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='File Name')),
                ('upload_time', models.DateTimeField(auto_now=True, verbose_name='Upload Time')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='casefiles', to='cases.Case', verbose_name='Case File')),
            ],
            options={
                'verbose_name': 'Case File',
                'verbose_name_plural': 'Case File',
                'ordering': ('-type', '-upload_time'),
            },
        ),
        migrations.CreateModel(
            name='TempFile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('case_uuid', models.UUIDField(verbose_name='UUID')),
                ('file', models.FileField(storage=storages.backends.gcloud.GoogleCloudStorage(bucket_name='froggy-service-temp'), upload_to='', verbose_name='Temp file')),
                ('file_name', models.CharField(blank=True, editable=False, max_length=255, null=True, verbose_name='File Name')),
                ('size', models.PositiveIntegerField(editable=False, verbose_name='Size')),
                ('upload_time', models.DateTimeField(auto_now=True, verbose_name='Upload Time')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tempfiles', to=settings.AUTH_USER_MODEL, verbose_name='Temp File')),
            ],
            options={
                'verbose_name': 'Case File',
                'verbose_name_plural': 'Case File',
            },
        ),
    ]
