# Generated by Django 3.2.16 on 2023-08-01 07:30

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('booking', '0007_alter_booking_class_trainers'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Booking_class',
            new_name='BookingClass',
        ),
    ]