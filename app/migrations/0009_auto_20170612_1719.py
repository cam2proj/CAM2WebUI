# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-12 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170612_1444'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publication',
            name='paperlink',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
