# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 09:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodAll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, choices=[(b'Lunch', 'Lunch'), (b'Dinner', 'Dinner')], max_length=200, null=True)),
                ('avail_datetime', models.DateTimeField(blank=True, null=True)),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Employee')),
            ],
        ),
    ]
