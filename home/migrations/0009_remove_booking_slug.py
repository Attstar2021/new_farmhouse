# Generated by Django 5.0 on 2023-12-06 21:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_room_roomcategory_remove_hotel_amenities_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='slug',
        ),
    ]
