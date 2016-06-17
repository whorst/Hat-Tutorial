# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-07 17:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name_field', models.CharField(max_length=200)),
                ('last_name_field', models.CharField(max_length=200)),
                ('email_field', models.CharField(max_length=200)),
                ('phone_number_field', models.CharField(max_length=12)),
                ('buy_options_field', models.CharField(choices=[('Shirt', 'shirt'), ('Frisbee', 'frisbee')], max_length=200)),
            ],
        ),
    ]
