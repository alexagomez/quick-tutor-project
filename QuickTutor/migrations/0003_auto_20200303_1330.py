# Generated by Django 3.0.2 on 2020-03-03 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0002_auto_20200302_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentrequest',
            name='confusionMeter',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentrequest',
            name='meetingDetails',
            field=models.CharField(default='', max_length=100),
        ),
    ]
