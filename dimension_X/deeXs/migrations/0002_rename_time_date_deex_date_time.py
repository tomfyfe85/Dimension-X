# Generated by Django 5.0.3 on 2024-03-16 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deeXs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='deex',
            old_name='time_date',
            new_name='date_time',
        ),
    ]
