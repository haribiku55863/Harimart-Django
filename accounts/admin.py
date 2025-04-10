from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class AccountAdmin(UserAdmin):
    list_display=('email','first_name','last_name','username','last_login','date_joined','is_active')
    list_display_links=('email','first_name','last_name',)
    readonly_fields=('last_login','date_joined')
    ordering=('-date_joined',)
    filter_horizontal=()
    list_filter=()
    fieldsets=()
admin.site.register(Account,AccountAdmin)




'''

from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

class AccountAdmin(UserAdmin):
    # Displayed fields in the user list view
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'date_joined', 'is_active')

    # Fields to be displayed on the user detail page
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'username', 'phone_number')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Add filters to the right sidebar
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'date_joined')

    # Allow searching by email and username
    search_fields = ('email', 'username')

    # Allow sorting by date_joined or any other field
    ordering = ('-date_joined',)

    # Makes user creation easier by customizing the form to exclude non-required fields
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'username', 'phone_number', 'is_active', 'is_staff', 'is_superuser'),
        }),
    )

    filter_horizontal = ()  # No filters needed here for now

admin.site.register(Account, AccountAdmin)'''
