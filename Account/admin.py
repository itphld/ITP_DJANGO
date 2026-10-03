from django.contrib import admin
from .models import Account
# Register your models here.
class AccountAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','email','mobile','is_active','is_superuser','is_staff')
    readonly_fields=('last_login','date_joined')
    list_filter = ('is_active','is_superuser')
    list_editable = ('is_active','is_staff','is_superuser')
admin.site.register(Account,AccountAdmin)
