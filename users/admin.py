# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

# Custom User Admin class to manage the `CustomUser` model
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    # Fields to display in the list view
    list_display = ('username', 'email', 'can_access_contact', 'can_access_sales', 'can_access_purchase', 'can_access_account', 'is_active', 'is_staff')

    # Fields to include when editing a user
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('can_access_contact', 'can_access_sales', 'can_access_purchase', 'can_access_account')
        }),
    )

    # Fields to include when adding a new user
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': ('can_access_contact', 'can_access_sales', 'can_access_purchase', 'can_access_account')
        }),
    )

    # List filters to filter users by permissions
    list_filter = ('can_access_contact', 'can_access_sales', 'can_access_purchase', 'can_access_account', 'is_staff', 'is_active')

    # Search fields to search users by username or email
    search_fields = ('username', 'email')

    # Ordering of users
    ordering = ('username',)

# Register the CustomUser model with the custom admin interface
admin.site.register(CustomUser, CustomUserAdmin)
