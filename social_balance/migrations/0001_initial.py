# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-09-25 10:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0019_deletionprocess'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntitySocialBalance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_exempt', models.BooleanField(default=False, verbose_name='Est\xe1 exenta')),
                ('is_public', models.BooleanField(default=True, verbose_name='Informe p\xfablico')),
                ('done', models.BooleanField(default=False, verbose_name='Realizado')),
                ('year', models.SmallIntegerField(default=2019, verbose_name='A\xf1o')),
                ('external_id', models.CharField(blank=True, max_length=200, null=True, verbose_name='Identificador externo')),
                ('entity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='social_balances', to='accounts.Entity', verbose_name='Realizado por')),
            ],
            options={
                'verbose_name': 'Informe de balance social',
                'verbose_name_plural': 'Informes de balance social',
            },
        ),
    ]