# Generated by Django 3.2.5 on 2021-08-16 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concertapp', '0022_performanceseat_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performanceseat',
            name='price',
            field=models.IntegerField(default=100),
        ),
    ]
