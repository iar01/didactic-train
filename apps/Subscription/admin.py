from django.contrib import admin
from .models import *


class SubscriptionAdmin(admin.ModelAdmin):
    readonly_fields = ["Transaction_ID", "PaymentMethod"]

    
admin.site.register(Subscription, SubscriptionAdmin)
