# Generated by Django 3.2.16 on 2023-01-10 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_booking_class_trainers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking_class',
            old_name='call_date',
            new_name='requested_date',
        ),
        migrations.RenameField(
            model_name='booking_class',
            old_name='call_time',
            new_name='requested_time',
        ),
    ]
