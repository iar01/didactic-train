# Generated by Django 3.2.5 on 2021-07-16 12:52

from django.db import migrations, models
import location_field.models.plain


class Migration(migrations.Migration):

    dependencies = [
        ('QLA', '0002_alter_school_urn'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='Location',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='city',
            field=location_field.models.plain.PlainLocationField(max_length=63, null=True),
        ),
    ]