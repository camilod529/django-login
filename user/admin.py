from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import Textarea, TextInput, CharField
from django import forms
from user.models import CustomUser


# Register your models here.
class UserAdminConfig(UserAdmin):
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    model = CustomUser
    search_fields = ("email", "user_name", "first_name")
    list_filter = ("email", "user_name", "first_name", "is_active", "is_staff")
    ordering = ("-start_date",)
    list_display = ("email", "id", "user_name", "first_name", "is_active", "is_staff")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "user_name",
                    "first_name",
                ),
            },
        ),
        (
            "Permissions",
            {
                "fields": ("is_staff", "is_active"),
            },
        ),
    )
    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 20, "cols": 60})},
    }
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "user_name",
                    "first_name",
                    "password1",
                    "password2",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(CustomUser, UserAdminConfig)
