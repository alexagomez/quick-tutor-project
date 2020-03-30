# Generated by Django 3.0.2 on 2020-03-29 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentrequest',
            name='tutorEmail',
        ),
        migrations.RemoveField(
            model_name='studentrequest',
            name='tutorUsername',
        ),
        migrations.AddField(
            model_name='tutor',
            name='request',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='request', to='QuickTutor.StudentRequest'),
        ),
        migrations.DeleteModel(
            name='RequestCourse',
        ),
    ]
