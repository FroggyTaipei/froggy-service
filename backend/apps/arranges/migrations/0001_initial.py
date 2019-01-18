# Generated by Django 2.1.5 on 2019-01-18 13:12

import ckeditor_uploader.fields
from django.db import migrations, models
import django_fsm


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arrange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(choices=[('draft', '尚未發布'), ('published', '已發布')], default='draft', max_length=50, verbose_name='Arrange State')),
                ('title', models.CharField(max_length=120, verbose_name='Arrange Title')),
                ('content', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Content')),
                ('arrange_time', models.DateTimeField(blank=True, null=True, verbose_name='Arrange Time')),
                ('publish_time', models.DateTimeField(blank=True, null=True, verbose_name='Arrange Publish Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Time')),
                ('order', models.PositiveIntegerField()),
            ],
            options={
                'verbose_name': 'Arrange',
                'verbose_name_plural': 'Arrange',
                'ordering': ('-arrange_time',),
            },
        ),
    ]
