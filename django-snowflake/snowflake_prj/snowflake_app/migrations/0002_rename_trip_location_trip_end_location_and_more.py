# Generated by Django 5.1.6 on 2025-02-21 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snowflake_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trip',
            old_name='trip_location',
            new_name='end_location',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='trip_name',
            new_name='start_location',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='trip_description',
        ),
        migrations.AddField(
            model_name='trip',
            name='trip_duration',
            field=models.IntegerField(default=60),
        ),
    ]
