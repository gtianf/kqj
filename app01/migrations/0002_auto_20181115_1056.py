# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-11-15 02:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softtest',
            name='rom_id',
            field=models.CharField(max_length=30),
        ),
    ]
