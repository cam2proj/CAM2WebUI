# Generated by Django 2.0.6 on 2018-09-23 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0041_auto_20180923_1535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='subteam',
            field=models.CharField(blank=True, choices=[('I', 'Image Analysis'), ('UI', 'Web UI'), ('D+API', 'API team'), ('PP', 'Parrellel Perforamce'), ('RM', 'Reserouce Management'), ('SE', 'Software Engineering'), ('MA', 'Mobile App'), ('CR', 'Camera Reliability'), ('CD', 'Camera Discovery'), ('TL', 'Transfer Learning'), ('AT', 'Active Training LIst'), ('Intel', 'Embedded Computer Vision')], default='blank', max_length=50, verbose_name='Subteam'),
        ),
    ]
