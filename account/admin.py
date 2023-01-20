from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import *
# Register your models here.

@admin.register(Account)
class AccountAdmin(UserAdmin):
    fieldsets = (
        (None,{"fields":('email','phone','password')}),
        (
            _('Personal info'),
            {
                "fields":(
                    "first_name",
                    "last_name",
                    'type'
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields":("is_active", "is_staff", "is_superuser", "groups", "user_permissions")
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide"),
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "phone",
                    "type",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    list_display = ("first_name","last_name","phone","is_staff","date_joined","last_login")
    list_filter = ("is_staff","is_superuser","is_admin","is_superadmin","is_active")
    search_fields = ("first_name", "last_name","email", "phone")
    readonly_fields = ("date_joined","last_login")