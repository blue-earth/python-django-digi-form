# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-05-12 02:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160512_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='hero_image',
            field=models.ImageField(blank=True, null=True, upload_to=b'blog_uploads'),
        ),
    ]