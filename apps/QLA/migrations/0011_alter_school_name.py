# Generated by Django 3.2.5 on 2021-07-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QLA', '0010_alter_school_subjects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]