# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-21 15:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodwatch', '0003_auto_20181019_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='hood',
            name='count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
