# Generated by Django 3.0.3 on 2020-02-17 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ID',
            field=models.IntegerField(default=5050583, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='studentrequest',
            name='studentID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='studentrequest',
            name='tutorID',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='ID',
            field=models.IntegerField(default=4933044, primary_key=True, serialize=False),
        ),
    ]