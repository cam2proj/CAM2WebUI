# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-11-10 20:38
from __future__ import unicode_literals

import app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0049_auto_20181110_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('membername', models.CharField(max_length=50, validators=[app.validators.validateName], verbose_name='Member Name')),
                ('memberimg', models.CharField(blank=True, max_length=300, null=True, validators=[app.validators.validateURL], verbose_name='Member Image')),
                ('iscurrentmember', models.BooleanField(verbose_name='Is Current Member')),
                ('subteam', models.CharField(blank=True, choices=[('I', 'Image Analysis'), ('UI', 'Web UI'), ('D+API', 'API team'), ('PP', 'Parrellel Perforamce'), ('RM', 'Reserouce Management'), ('SE', 'Software Engineering'), ('MA', 'Mobile App'), ('CR', 'Camera Reliability'), ('CD', 'Camera Discovery'), ('TL', 'Transfer Learning'), ('AT', 'Active Training'), ('ID', 'Image Database'), ('DV', 'Drone Video'), ('FIA', 'Forest Inventory Analysis'), ('HB', 'Human Behavior'), ('CS', 'Crowdsourcing'), ('Intel', 'Embedded Computer Vision')], default='blank', max_length=50, verbose_name='Subteam')),
            ],
        ),
    ]
