# Generated by Django 3.2.5 on 2021-08-02 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subscription', '0011_auto_20210802_1937'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='City',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='State',
        ),
        migrations.AddField(
            model_name='subscription',
            name='Citi_data',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='City'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='Country_state',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='stateName',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='State'),
        ),
    ]
