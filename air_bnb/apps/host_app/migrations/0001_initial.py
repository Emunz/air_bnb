# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 21:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('review_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login_app.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Shows',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bands', models.TextField(null=True)),
                ('show_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Venues',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('venue_details', models.TextField(null=True)),
                ('space_name', models.CharField(max_length=255)),
                ('dry_zone', models.CharField(max_length=5)),
                ('noise_level', models.CharField(max_length=255)),
                ('capacity', models.IntegerField()),
                ('overnight_option', models.CharField(max_length=5)),
                ('suggested_donation', models.CharField(max_length=5)),
                ('promotions', models.CharField(max_length=5)),
                ('gear_availability', models.TextField()),
                ('show_start', models.TimeField()),
                ('show_end', models.TimeField()),
                ('bill_capacity', models.CharField(max_length=255)),
                ('location_type', models.CharField(max_length=255)),
                ('past_performers', models.TextField(null=True)),
                ('street_address', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('zip_code', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('host_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='login_app.Users')),
            ],
        ),
        migrations.AddField(
            model_name='shows',
            name='venue_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host_app.Venues'),
        ),
        migrations.AddField(
            model_name='reviews',
            name='venue_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='host_app.Venues'),
        ),
    ]
