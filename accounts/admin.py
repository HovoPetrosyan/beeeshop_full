from django.contrib import admin
from accounts.models import *
from django.contrib.auth.admin import UserAdmin


# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active',)
    list_display_links = ('email', 'first_name', 'last_name', 'username', )
    list_editable = ('is_active', )
    readonly_fields = ('last_login', 'date_joined', )
    ordering = ('-date_joined', )
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Account, AccountAdmin)