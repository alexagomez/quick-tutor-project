# Generated by Django 3.0.2 on 2020-02-22 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0007_auto_20200222_1551'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='USER_ID',
            field=models.IntegerField(default=2467489, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='USER_ID',
            field=models.IntegerField(default=3796419, primary_key=True, serialize=False),
        ),
    ]