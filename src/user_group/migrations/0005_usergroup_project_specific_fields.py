# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-22 05:20
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_group', '0004_auto_20171114_1117'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='project_specific_fields',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default=None, null=True),
        ),
    ]
