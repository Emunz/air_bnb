# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-25 21:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('host_app', '0002_auto_20171025_1846'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='musicians_id',
            new_name='user_id',
        ),
    ]
