# Generated by Django 3.2.5 on 2021-07-30 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bundle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Price', models.FloatField()),
                ('Discount', models.IntegerField()),
                ('Annual_Discount', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Bundle offers',
            },
        ),
    ]