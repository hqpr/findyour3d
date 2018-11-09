# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-09 14:30
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0018_auto_20180321_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='top_printing_processes',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[(0, 'Fused Deposition Modeling (FDM)'), (1, 'Selective Laser Melting / Direct Metal Laser Sintering (SLM / DMLS)'), (2, 'Selective Laser Sintering (SLS)'), (4, 'Binder Jetting (BJ) (Stone)'), (5, 'Electron Beam Melting (EBM) (Metals)'), (6, 'Stereolithography (SLA)'), (7, 'PolyJet / Material Jetting (MJ)'), (8, 'Various')], max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='website',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
