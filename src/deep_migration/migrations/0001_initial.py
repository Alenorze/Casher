# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-14 07:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geo', '0024_auto_20180107_0538'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminLevelMigration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('migrated_at', models.DateTimeField(auto_now_add=True)),
                ('level', models.IntegerField(unique=True)),
                ('admin_level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.AdminLevel')),
            ],
            options={
                'ordering': ['-migrated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CountryMigration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('migrated_at', models.DateTimeField(auto_now_add=True)),
                ('code', models.CharField(max_length=50, unique=True)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='geo.Region')),
            ],
            options={
                'ordering': ['-migrated_at'],
                'abstract': False,
            },
        ),
    ]