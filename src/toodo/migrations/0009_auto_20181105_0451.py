# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-11-05 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toodo', '0008_auto_20181104_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='document',
        ),
        migrations.AlterField(
            model_name='todo',
            name='created',
            field=models.DateField(default='2018-11-05'),
        ),
        migrations.AlterField(
            model_name='todo',
            name='due_date',
            field=models.DateField(default='2018-11-05'),
        ),
    ]
