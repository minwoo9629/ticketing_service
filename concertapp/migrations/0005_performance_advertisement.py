# Generated by Django 3.2.5 on 2021-07-23 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concertapp', '0004_performance_ticket_open_dt'),
    ]

    operations = [
        migrations.AddField(
            model_name='performance',
            name='advertisement',
            field=models.BooleanField(default=False),
        ),
    ]
