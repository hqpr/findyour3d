# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 13:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_remove_customer_is_functional_metal'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='is_advanced_filled',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_functional_or_basic',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'Yes, I want my project to be as functional as possible for the cost'), (2, 'No, I just need my projected to be printed very simply')], default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='plastic_concern',
            field=models.IntegerField(choices=[(0, 'None'), (1, 'My chief concern is cost'), (2, 'My chief concern is quality of the print')], default=0),
        ),
    ]
