# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-01-07 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_signupprocess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signupprocess',
            name='uuid',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, verbose_name='Identificador proceso'),
        ),
    ]