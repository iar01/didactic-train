# Generated by Django 3.2.5 on 2021-07-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contactus', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='Instagram',
            new_name='Twitter',
        ),
        migrations.AddField(
            model_name='contactus',
            name='Address',
            field=models.TextField(default='Hello'),
            preserve_default=False,
        ),
    ]