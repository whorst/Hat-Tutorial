# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-10 20:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0012_auto_20160610_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='phone_number',
            field=models.CharField(max_length=13),
        ),
    ]
