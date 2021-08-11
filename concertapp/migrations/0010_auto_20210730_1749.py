# Generated by Django 3.2.5 on 2021-07-30 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concertapp', '0009_alter_seat_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='seat',
            name='floor',
            field=models.CharField(default='스탠딩', max_length=10, verbose_name='층 수'),
        ),
        migrations.AddField(
            model_name='seat',
            name='row',
            field=models.IntegerField(default=1, verbose_name='오 와 열 중 열을 뜻함'),
        ),
    ]