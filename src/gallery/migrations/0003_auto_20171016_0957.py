# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-16 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20171016_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='is_public',
            field=models.BooleanField(default=True),
        ),
    ]
