# Generated by Django 3.2.16 on 2023-08-01 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0008_rename_booking_class_bookingclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingclass',
            name='trainers',
            field=models.CharField(default='Karol', max_length=20),
        ),
    ]