# Generated by Django 3.0 on 2021-09-05 14:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='post_details',
            new_name='post_detail',
        ),
    ]
