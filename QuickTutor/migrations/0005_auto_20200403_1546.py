# Generated by Django 3.0.3 on 2020-04-03 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0004_auto_20200403_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='balance',
            field=models.IntegerField(default=1000),
        ),
    ]