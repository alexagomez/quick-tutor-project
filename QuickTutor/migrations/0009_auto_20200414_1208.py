# Generated by Django 3.0.4 on 2020-04-14 16:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0008_auto_20200411_1630'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentrequest',
            name='sessionElapsedTime',
            field=models.TimeField(default=datetime.datetime(2020, 4, 14, 12, 8, 31, 204684)),
        ),
        migrations.AddField(
            model_name='studentrequest',
            name='sessionEndTime',
            field=models.TimeField(default=datetime.datetime(2020, 4, 14, 12, 8, 31, 204684)),
        ),
        migrations.AddField(
            model_name='studentrequest',
            name='sessionStartTime',
            field=models.TimeField(default=datetime.datetime(2020, 4, 14, 12, 8, 31, 204684)),
        ),
    ]
