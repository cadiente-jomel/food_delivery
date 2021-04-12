from django.contrib import admin
from .models import Customer, Profile
from django.contrib.auth.admin import UserAdmin

class CustomerAdminConfig(UserAdmin):
    search_fields = ('email', 'user_name', 'first_name')
    list_filter = ('email', 'user_name', 'first_name', 'is_active', 'is_superuser')
    ordering = ('-date_joined',)
    list_display = (
        'email', 'user_name', 'first_name', 'is_active', 'is_staff'
    )

    fieldsets = (
        ('Credentials', {'fields': ('email', 'user_name', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active',)}),
        ('Personal', {'fields': ('first_name', 'last_name',)})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_name', 'first_name', 'password1', 'password2', 
            'is_staff', 'is_active')
        }),
    )


admin.site.register(Customer, CustomerAdminConfig)
admin.site.register(Profile)
