# -*- coding: utf-8 -*-
# Generated by Django 1.11.28 on 2020-02-26 17:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0010_remove_null_blank_from_schedules_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='start',
            field=models.DateTimeField(db_index=True, default=None, help_text='Date this schedule went into effect', null=True),
        ),
    ]
