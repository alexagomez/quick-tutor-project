# Generated by Django 3.0.2 on 2020-02-22 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='USER_ID',
            field=models.IntegerField(default=8975588, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='USER_ID',
            field=models.IntegerField(default=9811719, primary_key=True, serialize=False),
        ),
    ]
