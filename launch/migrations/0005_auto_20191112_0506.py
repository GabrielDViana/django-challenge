# Generated by Django 2.2.7 on 2019-11-12 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launch', '0004_auto_20191112_0333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='launch',
            name='launch_date_local',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='launch',
            name='launch_date_utc',
            field=models.CharField(max_length=100),
        ),
    ]
