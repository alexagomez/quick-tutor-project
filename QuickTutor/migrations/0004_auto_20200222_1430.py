# Generated by Django 3.0.2 on 2020-02-22 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0003_auto_20200222_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='USER_ID',
            field=models.IntegerField(default=9136872, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='USER_ID',
            field=models.IntegerField(default=7905885, primary_key=True, serialize=False),
        ),
    ]
