# Generated by Django 3.2.16 on 2023-01-11 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0004_auto_20230110_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_class',
            name='requested_date',
            field=models.DateField(default='01-01-23'),
        ),
    ]
