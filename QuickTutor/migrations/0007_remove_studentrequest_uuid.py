# Generated by Django 3.0.3 on 2020-04-03 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0006_studentrequest_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentrequest',
            name='UUID',
        ),
    ]