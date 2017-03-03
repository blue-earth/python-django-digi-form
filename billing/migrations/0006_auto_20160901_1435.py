# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-01 04:35
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('billing', '0005_auto_20160822_1439'),
    ]

    operations = [
        migrations.CreateModel(
            name='StripeCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('card_id', models.CharField(max_length=64, null=True)),
                ('token_id', models.CharField(max_length=40, null=True)),
                ('card_brand', models.CharField(max_length=40, null=True)),
                ('card_country', models.CharField(max_length=40, null=True)),
                ('card_last4', models.CharField(max_length=4, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StripeCustomer',
            fields=[
                ('customer_id', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('raw_response', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='plansubscription',
            name='recurrence_period',
        ),
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(max_length=24, unique=True),
        ),
        migrations.AddField(
            model_name='stripecard',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='billing.StripeCustomer'),
        ),
    ]
