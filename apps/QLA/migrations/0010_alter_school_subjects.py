# Generated by Django 3.2.5 on 2021-07-28 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QLA', '0009_alter_school_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='subjects',
            field=models.ManyToManyField(to='QLA.Subject'),
        ),
    ]
