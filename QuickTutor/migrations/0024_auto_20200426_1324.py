# Generated by Django 3.0.2 on 2020-04-26 17:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0023_auto_20200426_1157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint',
            name='complainantUsername',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='complaint',
            name='complaineeUsername',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='studentrequest',
            name='requestTime',
            field=models.TimeField(default=datetime.datetime(2020, 4, 26, 13, 24, 14, 841820)),
        ),
        migrations.AlterField(
            model_name='studentrequest',
            name='sessionEndTime',
            field=models.TimeField(default=datetime.datetime(2020, 4, 26, 13, 24, 14, 842006)),
        ),
        migrations.AlterField(
            model_name='studentrequest',
            name='sessionStartTime',
            field=models.TimeField(default=datetime.datetime(2020, 4, 26, 13, 24, 14, 841977)),
        ),
        migrations.AlterField(
            model_name='studentrequest',
            name='studentUsername',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='studentrequest',
            name='tutorUsername',
            field=models.CharField(default='', max_length=100),
        ),
    ]