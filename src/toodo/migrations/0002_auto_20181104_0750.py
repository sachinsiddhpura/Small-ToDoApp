# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-11-04 07:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toodo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='contact_number',
            field=models.IntegerField(default=9090909090),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(default='School', on_delete=django.db.models.deletion.CASCADE, to='toodo.Category'),
        ),
    ]