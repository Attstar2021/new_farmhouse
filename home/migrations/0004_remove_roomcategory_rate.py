# Generated by Django 3.2.20 on 2023-12-02 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_comment_post_delete_guest_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roomcategory',
            name='rate',
        ),
    ]