# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-23 17:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_entity_profile_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entity',
            name='latitude',
            field=models.FloatField(default=40.48258477012512, verbose_name='Latitud'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='longitude',
            field=models.FloatField(default=-3.3641982078552246, verbose_name='Longitud'),
        ),
    ]
