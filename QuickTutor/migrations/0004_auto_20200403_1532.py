# Generated by Django 3.0.3 on 2020-04-03 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0003_auto_20200403_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tutor',
            name='balance',
            field=models.IntegerField(default=0),
        ),
    ]
