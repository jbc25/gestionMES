# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-23 13:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0007_cardpayment_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardpayment',
            name='bank_response',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sermepa.SermepaResponse', verbose_name='Respuesta TPV'),
        ),
    ]
