from django.contrib import admin
from django.utils.html import format_html
from .models import CustomUser, Event, Story


class StoryInline(admin.StackedInline):
    model = Story
    can_delete = False
    verbose_name_plural = 'Stories'
    fk_name = 'user'


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email_link', 'is_active', 'is_staff', 'is_superuser', 'story')
    fields = ('name', 'email', 'is_active', 'is_staff', 'is_superuser')
    inlines = [StoryInline]

    def email_link(self, obj):
        link = f'/admin/stories/customuser/{obj.id}/change/'
        return format_html(f'<a href="{link}">{obj.email}</a>')

    email_link.short_description = 'Email Address'


# Register the CustomUser model with its corresponding CustomUserAdmin


# Register Event and Story models with the default admin interface
admin.site.register(Event)


@admin.register(Story)
class StoryAdmin(admin.ModelAdmin):
    list_display = ('story_name', 'is_valid', 'user')
    fields = ('user', 'story_name', 'story_description', 'story_image', 'is_valid')
