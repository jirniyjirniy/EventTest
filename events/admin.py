from django.contrib import admin
from events.api.models import Event, Registration

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'location', 'organizer', 'created_at', 'updated_at')
    list_filter = ('date', 'location', 'organizer')
    search_fields = ('title', 'description', 'location')
    ordering = ('-date',)
    date_hierarchy = 'date'
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'date', 'location', 'organizer')
        }),
        ('Timestamp', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',),
        }),
    )


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'user', 'registered_at')
    list_filter = ('event', 'user', 'registered_at')
    search_fields = ('event__title', 'user__username')
    ordering = ('-registered_at',)
    date_hierarchy = 'registered_at'
