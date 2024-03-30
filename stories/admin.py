from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Event, Story


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ["email", "name"]  # Adjusted to display email and name
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('name',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('name',)}),
    )
    search_fields = ['email', 'name']
    ordering = ['email']


# Register the CustomUser model with its corresponding CustomUserAdmin
admin.site.register(CustomUser)

# Register Event and Story models with the default admin interface
admin.site.register(Event)
admin.site.register(Story)
