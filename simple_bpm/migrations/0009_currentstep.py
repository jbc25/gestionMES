# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-15 13:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_bpm', '0008_workflow_ordering'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currentprocessstep',
            name='shortname',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Nombre corto'),
        ),
    ]
