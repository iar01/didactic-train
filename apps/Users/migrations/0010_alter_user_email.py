# Generated by Django 3.2.5 on 2021-07-28 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0009_auto_20210728_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
