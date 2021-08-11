# Generated by Django 3.2.5 on 2021-08-11 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concertapp', '0016_remove_seat_reserve'),
        ('reservationapp', '0003_auto_20210811_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='seat',
            field=models.ForeignKey(blank=True, limit_choices_to={'reservation': False}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='concertapp.seat'),
        ),
    ]
