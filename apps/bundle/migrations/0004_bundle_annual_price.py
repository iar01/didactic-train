# Generated by Django 3.2.5 on 2021-07-30 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bundle', '0003_auto_20210730_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='bundle',
            name='Annual_Price',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]