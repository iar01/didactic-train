# Generated by Django 3.2.5 on 2021-07-16 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('QLA', '0003_auto_20210716_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='country',
            name='loc_lat',
        ),
        migrations.RemoveField(
            model_name='country',
            name='loc_long',
        ),
    ]
