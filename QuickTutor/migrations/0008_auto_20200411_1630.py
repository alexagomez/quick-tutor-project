# Generated by Django 3.0.3 on 2020-04-11 20:30

import QuickTutor.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0007_remove_studentrequest_uuid'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=QuickTutor.models.get_image_path),
        ),
        migrations.AddField(
            model_name='tutor',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=QuickTutor.models.get_image_path),
        ),
    ]
