# Generated by Django 3.2.5 on 2021-07-15 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20210715_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='AccountOwner',
            field=models.BooleanField(default=False),
        ),
    ]
