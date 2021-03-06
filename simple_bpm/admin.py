# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from simple_bpm.models import ProcessStepTask, ProcessStep, Process, CurrentProcess, CurrentProcessStep, ProcessWorkflow


class ChecklistInline(admin.TabularInline):
    model = ProcessStepTask

class ProcessStepAdmin(admin.ModelAdmin):
    list_display = ('process', 'title')
    inlines = [
        ChecklistInline,
    ]


admin.site.register(ProcessStep, ProcessStepAdmin)
admin.site.register(Process)
admin.site.register(CurrentProcess)
admin.site.register(CurrentProcessStep)
admin.site.register(ProcessWorkflow)
