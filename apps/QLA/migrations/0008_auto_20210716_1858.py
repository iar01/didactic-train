# Generated by Django 3.2.5 on 2021-07-16 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('QLA', '0007_alter_paper_grade_boundaries'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_questions',
            field=models.FileField(blank=True, upload_to='Topic/'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='topic_solutions',
            field=models.FileField(blank=True, upload_to='Topic/'),
        ),
    ]
