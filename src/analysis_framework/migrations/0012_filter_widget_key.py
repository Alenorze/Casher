# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-26 15:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_framework', '0011_auto_20171211_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='filter',
            name='widget_key',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
