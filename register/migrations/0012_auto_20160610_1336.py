# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0011_auto_20160609_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='position',
            field=models.CharField(choices=[('In Cutter', 'In Cutter'), ('Out Cutter', 'Out Cutter'), ('Short Distance Handler', 'Short Distance Handler'), ('Long Distanc Handler', 'Long Distance Handler')], default='In Cutter', max_length=200),
        ),
        migrations.AlterField(
            model_name='person',
            name='skill',
            field=models.CharField(choices=[('1', '1   Amateur'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5   Pro')], default='1', max_length=200),
        ),
    ]
