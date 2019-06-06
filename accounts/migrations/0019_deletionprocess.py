# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-06-06 17:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('simple_bpm', '0010_workflow_state_null'),
        ('accounts', '0018_signupprocess_cancelled'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeletionProcess',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(auto_created=True, default=uuid.uuid4, verbose_name='Identificador proceso')),
                ('last_update', models.DateTimeField(auto_now=True, verbose_name='\xdaltima actualizaci\xf3n')),
                ('member_type', models.CharField(blank=True, choices=[(b'consumidora', b'Socia consumidora'), (b'colaboradora', b'Socia colaboradora'), (b'proveedora', b'Socia proveedora')], max_length=30, null=True, verbose_name='Tipo de socia')),
                ('cancelled', models.BooleanField(default=False, verbose_name='Cancelado')),
                ('account', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='deletion_process', to='accounts.Account', verbose_name='Datos de socia')),
                ('workflow', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='simple_bpm.ProcessWorkflow', verbose_name='Seguimiento del proceso')),
            ],
            options={
                'verbose_name': 'Proceso de baja',
                'verbose_name_plural': 'Procesos de baja',
                'permissions': (('mespermission_can_view_deletions', 'Puede ver los procesos de baja pendientes'), ('mespermission_can_create_deletions', 'Puede a\xf1adir nuevos procesos de baja'), ('mespermission_can_comment_deletions', 'Puede a\xf1adir comentarios a un proceso de baja'), ('mespermission_can_update_deletions', 'Puede actualizar el estado de un proceso de baja')),
            },
        ),
    ]
