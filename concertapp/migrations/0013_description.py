# Generated by Django 3.2.5 on 2021-07-31 17:19

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('concertapp', '0012_alter_seat_row'),
    ]

    operations = [
        migrations.CreateModel(
            name='Description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True)),
                ('performance', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='concertapp.performance')),
            ],
        ),
    ]