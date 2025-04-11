import django_filters
from events.api.models import Event

class EventFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(field_name='location', lookup_expr='icontains')
    date_from = django_filters.DateTimeFilter(field_name='date', lookup_expr='gte')
    date_to = django_filters.DateTimeFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Event
        fields = ['date_from', 'date_to', 'location', 'organizer']
