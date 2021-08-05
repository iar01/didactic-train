from django.contrib import admin
from .models import *


class BundleAdmin(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Price', 'Discount', 'Annual_Discount', 'Annual_Price')
    search_fields = ('id', 'Name', 'Price', 'Discount', 'Annual_Discount', 'Annual_Price')
    readonly_fields = ('Annual_Price',)


admin.site.register(Bundle, BundleAdmin)
admin.site.register(Points)
