from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, FilteredEventsList

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('events_filter/', FilteredEventsList.as_view(), name='filtered_events'),
]
