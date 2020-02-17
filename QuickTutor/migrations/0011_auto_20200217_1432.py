# Generated by Django 3.0.3 on 2020-02-17 19:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0010_auto_20200212_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='matchedID',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='studentrequest',
            name='studentID',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='studentrequest',
            name='tutorID',
            field=models.UUIDField(default=uuid.uuid4),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='matchedID',
            field=models.UUIDField(default=uuid.uuid4),
        ),
    ]
