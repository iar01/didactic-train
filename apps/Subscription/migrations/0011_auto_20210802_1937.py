# Generated by Django 3.2.5 on 2021-08-02 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('QLA', '0012_alter_school_subjects'),
        ('Subscription', '0010_subscription_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='City',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='Country',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='EndDate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='PaymentMethod',
            field=models.CharField(blank=True, choices=[('Paypal', 'Paypal'), ('Stripe', 'Stripe')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='Price',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='School',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='QLA.school'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='State',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='Subject',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='QLA.subject'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='Transaction_ID',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='email',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='firstName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='lastName',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='phone',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]