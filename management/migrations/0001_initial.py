# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-03 18:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label_color', models.CharField(blank=True, default='#FFFFFF', max_length=20)),
                ('group', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
            options={
                'verbose_name': 'Comisi\xf3n',
                'verbose_name_plural': 'Comisiones',
            },
        ),
    ]