# Generated by Django 3.2.5 on 2021-07-30 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concertapp', '0010_auto_20210730_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat',
            name='row',
            field=models.IntegerField(null=True, verbose_name='오 와 열 중 열을 뜻함'),
        ),
    ]
