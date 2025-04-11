from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from rest_framework import viewsets, permissions, status, generics, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.core.mail import send_mail
from django.conf import settings

from utils.filters import EventFilter
from .models import Event, Registration
from .serializers import EventSerializer, RegistrationSerializer, UserSerializer


class EventViewSet(viewsets.ModelViewSet):
    """
    A viewset to handle CRUD operations for events.
    Supports filtering by date, location, and organizer.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['date', 'location', 'organizer']
    search_fields = ['title', 'description', 'location']

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def register(self, request, pk=None):
        """
        Custom action to register the current user for an event.
        Prevents duplicate registrations and sends an email notification.
        """
        event = self.get_object()
        if Registration.objects.filter(event=event, user=request.user).exists():
            return Response({'detail': 'Already registered for this event.'}, status=status.HTTP_400_BAD_REQUEST)
        registration = Registration.objects.create(event=event, user=request.user)

        # Send email notification (make sure to configure email backend in settings)
        subject = f"Registration Confirmed: {event.title}"
        message = (
            f"Hello {request.user.username},\n\n"
            f"You have successfully registered for '{event.title}' scheduled on {event.date} at {event.location}.\n\n"
            "Thank you!"
        )
        recipient_list = [request.user.email]
        send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list, fail_silently=True)

        serializer = RegistrationSerializer(registration)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


# User registration view
class UserRegistrationView(generics.CreateAPIView):
    """
    API endpoint for new user registration.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class FilteredEventsList(generics.ListAPIView):
    """
     A separate API endpoint that returns a list of events,
    filtered by parameters passed in query string.
    """
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = EventFilter
    filterset_fields = ['location', 'organizer']
    search_fields = ['title', 'description', 'location']


class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post', 'head', 'options']