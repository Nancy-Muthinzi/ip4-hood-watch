# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodwatch', '0008_auto_20181022_1408'),
    ]

    operations = [
        migrations.AddField(
            model_name='hood',
            name='hood_image',
            field=models.ImageField(null=True, upload_to='hood/'),
        ),
    ]
