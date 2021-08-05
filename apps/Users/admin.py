from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as UserAdmin
from .models import *


class UserAdminModel(UserAdmin):
    def make_active(self, request, queryset):
        queryset.update(is_active=True)

    make_active.short_description = 'Mark Selected user as active'

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)

    make_inactive.short_description = 'Mark Selected user as inactive'

    model = User
    list_display = (
        'id', 'username', 'email', 'firstname', 'lastname', 'is_active', 'is_staff', 'AccountOwner',
        'created_at',
        'updated_at')

    search_fields = ('id', 'email', 'username')

    fieldsets = (
        ('Basic Info', {'fields': ('email', 'username', 'password')}),
        ('Personal info', {'fields': (
            'firstname', 'lastname', 'date_of_birth', 'pic', 'School', 'gender', 'type_of_user', 'Country')}),
        ('Permission', {'fields': ('is_superuser', 'is_staff', 'AccountOwner', 'is_active')})
    )
    add_fieldsets = (
        (
            None, {
                'classes': ('wide',),
                'fields': ('email', 'password1', 'password2', 'is_active', 'is_staff', 'groups')
            }
        ),
    )
    actions = [make_active, make_inactive]


admin.site.register(User, UserAdminModel)
