# Generated by Django 3.2.5 on 2021-08-13 16:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('reservationapp', '0012_alter_reservation_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
