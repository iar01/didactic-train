# Generated by Django 3.2.5 on 2021-07-30 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bundle', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Points',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Point', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Points',
            },
        ),
        migrations.AddField(
            model_name='bundle',
            name='Point',
            field=models.ManyToManyField(to='bundle.Points'),
        ),
    ]
