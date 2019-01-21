# Generated by Django 2.1.5 on 2019-01-21 11:16

from django.db import migrations, models
import django.db.models.deletion
import django_fsm
import tagulous.models.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(choices=[('draft', '尚未成案'), ('disapproved', '不受理'), ('arranged', '處理中'), ('closed', '已結案')], default='draft', max_length=50, verbose_name='Case State')),
                ('uuid', models.UUIDField(default=uuid.uuid4, unique=True, verbose_name='UUID')),
                ('number', models.CharField(blank=True, default='-', max_length=6, null=True, verbose_name='Case Number')),
                ('title', models.CharField(max_length=255, verbose_name='Case Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Location')),
                ('username', models.CharField(max_length=50, verbose_name='Username')),
                ('mobile', models.CharField(blank=True, max_length=10, null=True, verbose_name='Mobile')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('open_time', models.DateTimeField(blank=True, null=True, verbose_name='Opened Time')),
                ('close_time', models.DateTimeField(blank=True, null=True, verbose_name='Closed Time')),
                ('create_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Created Time')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Time')),
                ('disapprove_info', models.TextField(blank=True, null=True, verbose_name='Disapprove Info')),
                ('note', models.TextField(blank=True, null=True, verbose_name='Case Notes')),
            ],
            options={
                'verbose_name': 'Case',
                'verbose_name_plural': 'Cases',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='CaseHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(choices=[('draft', '尚未成案'), ('disapproved', '不受理'), ('arranged', '處理中'), ('closed', '已結案')], default='draft', max_length=50, protected=True, verbose_name='Case State')),
                ('title', models.CharField(max_length=255, verbose_name='Case Title')),
                ('content', models.TextField(verbose_name='Content')),
                ('location', models.CharField(blank=True, max_length=255, null=True, verbose_name='Location')),
                ('username', models.CharField(max_length=50, verbose_name='Username')),
                ('mobile', models.CharField(blank=True, max_length=10, null=True, verbose_name='Mobile')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Address')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='case_histories', to='cases.Case', verbose_name='Case')),
            ],
            options={
                'verbose_name': 'Case History',
                'verbose_name_plural': 'Case Histories',
                'ordering': ('-create_time',),
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Time')),
            ],
            options={
                'verbose_name': 'User Region',
                'verbose_name_plural': 'User Region',
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Tagulous_Case_tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField()),
                ('count', models.IntegerField(default=0, help_text='Internal counter of how many times this tag is in use')),
                ('protected', models.BooleanField(default=False, help_text='Will not be deleted when the count reaches 0')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
            bases=(tagulous.models.models.BaseTagModel, models.Model),
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('update_time', models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Time')),
            ],
            options={
                'verbose_name': 'Case Type',
                'verbose_name_plural': 'Case Type',
                'ordering': ('id',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='tagulous_case_tags',
            unique_together={('slug',)},
        ),
    ]
