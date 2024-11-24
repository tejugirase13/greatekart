from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account

class AccountAdmin(UserAdmin):
    List_display = ('email','first_name','username','email','is_active','date_joined')
    List_display_Links = ('first_name','username','email')
    readonly_fields = ('last_joined','password')  #readonly mode password

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


#register your models here

admin.site.register(Account,AccountAdmin)
