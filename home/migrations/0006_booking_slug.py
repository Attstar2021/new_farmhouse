# Generated by Django 5.0 on 2023-12-05 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20231204_2354'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='slug',
            field=models.SlugField(max_length=200, null=True, unique=True),
        ),
    ]