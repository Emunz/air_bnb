# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 16:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musician_app', '0003_musicians_show_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musicians',
            old_name='show_id',
            new_name='show',
        ),
        migrations.RenameField(
            model_name='musicians',
            old_name='musician_id',
            new_name='user',
        ),
    ]
