# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-14 11:12
from __future__ import unicode_literals

from django.db import migrations


def remove_non_unique_memberships(apps, schema_editor):
    GroupMembership = apps.get_model('user_group', 'GroupMembership')
    for row in GroupMembership.objects.all():
        if GroupMembership.objects.filter(member=row.member,group=row.group).count() > 1:
            row.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('user_group', '0002_auto_20170907_0949'),
    ]

    operations = [
        migrations.RunPython(remove_non_unique_memberships),
    ]