# Generated by Django 3.2.5 on 2021-08-11 17:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concertapp', '0018_remove_seat_reserve'),
        ('reservationapp', '0006_alter_reservation_seat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='seat',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='concertapp.seat'),
        ),
    ]
