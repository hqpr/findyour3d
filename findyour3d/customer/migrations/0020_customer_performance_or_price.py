# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-27 09:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0019_auto_20171001_0824'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='performance_or_price',
            field=models.IntegerField(choices=[(0, 'Unknown'), (1, 'No, I want the very best quality for the price'), (2, "Yes, I'd settle for a little less quality for a little less of the cost")], default=0),
        ),
    ]