# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0010_auto_20160609_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('Pref', 'Prefer Not to Respond')], max_length=100),
        ),
    ]
