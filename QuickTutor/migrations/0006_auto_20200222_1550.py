# Generated by Django 3.0.2 on 2020-02-22 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QuickTutor', '0005_auto_20200222_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='student',
            name='USER_ID',
            field=models.IntegerField(default=7240589, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tutor',
            name='USER_ID',
            field=models.IntegerField(default=6902319, primary_key=True, serialize=False),
        ),
    ]
