# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 07:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entry', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-modified_at', '-created_at'], 'verbose_name_plural': 'entries'},
        ),
    ]
