# Generated by Django 3.0.3 on 2020-02-17 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0002_auto_20200217_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='ID',
            field=models.IntegerField(default=7216605, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='ID',
            field=models.IntegerField(default=6267664, primary_key=True, serialize=False),
        ),
    ]