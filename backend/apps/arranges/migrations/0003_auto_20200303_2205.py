# Generated by Django 2.2.10 on 2020-03-03 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arranges', '0002_arrange_case'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arrange',
            name='order',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Order'),
        ),
    ]
