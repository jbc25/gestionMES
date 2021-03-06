# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-02-21 21:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='payment_conditions',
            field=models.TextField(blank=True, null=True, verbose_name='Condiciones uso Etics'),
        ),
        migrations.AlterField(
            model_name='account',
            name='pay_by_debit',
            field=models.BooleanField(default=False, help_text='Permito que el MES domicilie en mi cuenta bancaria mi cuota anual y el capital social', verbose_name='Domiciliar la cuota'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='highest_salary',
            field=models.FloatField(blank=True, null=True, verbose_name='Salario bruto anual m\xe1s alto'),
        ),
        migrations.AlterField(
            model_name='entity',
            name='lowest_salary',
            field=models.FloatField(blank=True, null=True, verbose_name='Salario bruto anual m\xe1s bajo'),
        ),
    ]
