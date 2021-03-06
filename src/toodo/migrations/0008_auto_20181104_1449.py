# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-11-04 14:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toodo', '0007_auto_20181104_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='document',
            field=models.FileField(default='School', upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='toodo.Category'),
        ),
    ]
