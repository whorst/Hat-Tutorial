# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-09 13:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0005_auto_20160608_1616'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Choices',
            new_name='BuyOptions',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='the_choices',
            new_name='buy_options',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='email_field',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='first_name_field',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='last_name_field',
            new_name='last_name',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='phone_number_field',
            new_name='phone_number',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='sex_field',
            new_name='sex',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='shirt_size_field',
            new_name='shirt_size',
        ),
        migrations.RenameField(
            model_name='person',
            old_name='skill_field',
            new_name='skill',
        ),
    ]