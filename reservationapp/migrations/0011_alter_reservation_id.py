# Generated by Django 3.2.5 on 2021-08-13 16:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reservationapp', '0010_auto_20210811_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]