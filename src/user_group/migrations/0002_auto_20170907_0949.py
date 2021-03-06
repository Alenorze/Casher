# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-07 09:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMembership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(choices=[('normal', 'Normal'), ('admin', 'Admin')], default='normal', max_length=100)),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='usergroup',
            name='members',
        ),
        migrations.AddField(
            model_name='usergroup',
            name='members',
            field=models.ManyToManyField(blank=True, through='user_group.GroupMembership', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupmembership',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_group.UserGroup'),
        ),
        migrations.AddField(
            model_name='groupmembership',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
