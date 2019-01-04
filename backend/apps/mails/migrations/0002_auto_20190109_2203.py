# Generated by Django 2.1.5 on 2019-01-09 14:03

import django.contrib.postgres.fields.hstore
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cases', '0001_initial'),
        ('mails', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendGridMail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_email', models.EmailField(max_length=254, verbose_name='To Email')),
                ('to_email', models.EmailField(max_length=254, verbose_name='To Email')),
                ('data', django.contrib.postgres.fields.hstore.HStoreField(verbose_name='Mail Data')),
                ('success', models.BooleanField(default=False, verbose_name='Request Success')),
                ('send_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Send Time')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sendgrid_mails', to='cases.Case', verbose_name='Case')),
            ],
            options={
                'verbose_name': 'SendGrid Mail',
                'verbose_name_plural': 'SendGrid Mails',
                'ordering': ('-send_time',),
            },
        ),
        migrations.CreateModel(
            name='SendGridMailTemplate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.CharField(max_length=255, verbose_name='Template Id')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Time')),
            ],
            options={
                'verbose_name': 'SendGrid Template',
                'verbose_name_plural': 'SendGrid Template',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='sendgridmail',
            name='template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mails', to='mails.SendGridMailTemplate', verbose_name='SendGrid Template'),
        ),
    ]
