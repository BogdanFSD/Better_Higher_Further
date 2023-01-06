# Generated by Django 3.2.16 on 2023-01-04 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_class',
            name='status',
            field=models.CharField(choices=[('confirmed', 'confirmed'), ('rejected', 'rejected'), ('In progress', 'In progress')], default='In progress', max_length=15),
        ),
        migrations.AlterField(
            model_name='booking_class',
            name='call_time',
            field=models.CharField(choices=[('09:00', '09:00'), ('10:00', '10:00'), ('11:00', '11:00'), ('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00')], default='10:00', max_length=10),
        ),
    ]
