# Generated by Django 3.0.4 on 2020-04-26 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0022_auto_20200422_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrequest',
            name='requestTime',
            field=models.TimeField(default=datetime.datetime(2020, 4, 26, 11, 57, 6, 325281)),
        ),
        migrations.AlterField(
            model_name='studentrequest',
            name='sessionEndTime',
            field=models.TimeField(default=datetime.datetime(2020, 4, 26, 11, 57, 6, 326279)),
        ),
        migrations.AlterField(
            model_name='studentrequest',
            name='sessionStartTime',
            field=models.TimeField(default=datetime.datetime(2020, 4, 26, 11, 57, 6, 326279)),
        ),
    ]
