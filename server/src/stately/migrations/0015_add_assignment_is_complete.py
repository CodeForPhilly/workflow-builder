# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stately', '0014_allow_null_actor_on_assignments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='valid',
            new_name='is_valid',
        ),
        migrations.AddField(
            model_name='assignment',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='assignment',
            name='case',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assignments', to='stately.Case'),
        ),
    ]
