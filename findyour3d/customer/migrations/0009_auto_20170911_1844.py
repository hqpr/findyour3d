# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-11 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_auto_20170911_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_type',
            field=models.IntegerField(choices=[(0, 'Individual'), (1, 'A Small Business'), (2, 'Industrial Business')], default=0),
        ),
    ]
