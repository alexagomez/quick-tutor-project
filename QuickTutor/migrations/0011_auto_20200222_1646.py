# Generated by Django 3.0.2 on 2020-02-22 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0010_auto_20200222_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='USER_ID',
            field=models.IntegerField(default=1157911, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='USER_ID',
            field=models.IntegerField(default=8519407, primary_key=True, serialize=False),
        ),
    ]