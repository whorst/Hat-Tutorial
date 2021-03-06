# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0007_auto_20160609_0939'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BuyOptions',
            new_name='FrisbeeOptions',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='buy_options',
            new_name='shirt_options',
        ),
        migrations.AddField(
            model_name='person',
            name='frisbee_options',
            field=models.ManyToManyField(to='register.FrisbeeOptions'),
        ),
    ]
