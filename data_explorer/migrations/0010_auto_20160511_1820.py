# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-11 08:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_explorer', '0009_auto_20160510_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='justiceofpeace',
            name='mobile_number',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='Mobile Number'),
        ),
    ]