# Generated by Django 3.0.2 on 2020-03-01 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0002_auto_20200223_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='username',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='tutor',
            name='username',
            field=models.CharField(default='', max_length=10),
        ),
    ]