# Generated by Django 3.2.5 on 2021-08-11 17:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('concertapp', '0017_seat_reserve'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seat',
            name='reserve',
        ),
    ]
