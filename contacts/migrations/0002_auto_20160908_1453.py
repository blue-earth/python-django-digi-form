# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-08 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(0, 'M'), (1, 'F')], null=True),
        ),
    ]
