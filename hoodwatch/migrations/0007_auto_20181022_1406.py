# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-22 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoodwatch', '0006_auto_20181022_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hood',
            name='hood_location',
            field=models.CharField(choices=[('Westlands', 'Westlands Constituency'), ('Dagoretti', 'Dagoretti Constituency'), ('Dagoretti', 'Dagoretti Constituency'), ('Langata', 'Langata Constituency'), ('Kasarani', 'Kasarani Constituency'), ('Embakasi', 'Embakasi Constituency'), ('Starehe', 'Starehe Constituency'), ('Kamkunji', 'Kamkunji Constituency')], max_length=25),
        ),
    ]
