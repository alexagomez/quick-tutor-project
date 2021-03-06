# Generated by Django 3.0.2 on 2020-04-17 20:14

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0018_auto_20200414_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrequest',
            name='sessionEndTime',
            field=models.TimeField(default=datetime.datetime(2020, 4, 17, 16, 14, 6, 636908)),
        ),
        migrations.AlterField(
            model_name='studentrequest',
            name='sessionStartTime',
            field=models.TimeField(default=datetime.datetime(2020, 4, 17, 16, 14, 6, 636871)),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='request',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='QuickTutor.StudentRequest'),
        ),
    ]
