from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from apps.QLA.models import Subject, School
from apps.bundle.models import Bundle

User = get_user_model()
PaymentMethod = settings.PAYMENT_METHOD


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    firstName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    Country_state = models.CharField('Country', max_length=100, null=True, blank=True)
    stateName = models.CharField('State', max_length=100, null=True, blank=True)
    Citi_data = models.CharField('City', max_length=100, null=True, blank=True)
    TimeStart = models.DateTimeField(auto_created=True, auto_now_add=True)
    Price = models.FloatField(null=True, blank=True)
    EndDate = models.DateTimeField(null=True, blank=True)
    Transaction_ID = models.CharField(max_length=100, null=True, blank=True)
    # order.id,
    bundle = models.ForeignKey(Bundle, on_delete=models.DO_NOTHING, null=True, blank=True)
    Subject = models.ForeignKey(Subject, on_delete=models.DO_NOTHING, null=True, blank=True)
    School = models.ForeignKey(School, on_delete=models.DO_NOTHING, null=True, blank=True)
    PaymentMethod = models.CharField(max_length=100, choices=PaymentMethod, null=True, blank=True)
    # for Paypal:
    order_status = models.CharField(max_length=255, help_text='For Paypal only', null=True, blank=True)
    order_time = models.CharField(max_length=255, help_text='For Paypal only', null=True, blank=True)
    order_payer_payer_id = models.CharField(max_length=255, help_text='For Paypal only', null=True, blank=True)
    order_payer_name_given_name = models.CharField(max_length=255, help_text='For Paypal only', null=True, blank=True)
    order_payer_name_surname = models.CharField(max_length=255, help_text='For Paypal only', null=True, blank=True)
    order_payer_phone = models.CharField(max_length=255, help_text='For Paypal only', null=True, blank=True)
    order_payer_birth_date = models.CharField(max_length=255, help_text='For Paypal only', null=True, blank=True)
    order_payer_email_address = models.CharField(max_length=255, help_text='For Paypal only', null=True, blank=True)
    order_purchase_units_amount_currency_code = models.CharField(max_length=255, help_text='For Paypal only', null=True,
                                                                 blank=True)
    order_purchase_units_amount_value = models.CharField(max_length=255, help_text='For Paypal only', null=True,
                                                         blank=True)
    order_purchase_units_payee_email_address = models.CharField(max_length=255, help_text='For Paypal only', null=True,
                                                                blank=True)
    order_purchase_units_payee_merchant_id = models.CharField(max_length=255, help_text='For Paypal only', null=True,
                                                              blank=True)

    class Meta:
        verbose_name_plural = 'Subscription'

    def __str__(self):
        return "{} - {}".format(self.id, self.user)
