from rest_framework import serializers
from .models import Event, Registration
from django.contrib.auth.models import User

class EventSerializer(serializers.ModelSerializer):
    organizer = serializers.ReadOnlyField(source='organizer.username')

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'location', 'organizer', 'created_at', 'updated_at']

class RegistrationSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    event_detail = EventSerializer(source='event', read_only=True)

    class Meta:
        model = Registration
        fields = ['id', 'event', 'event_detail', 'user', 'registered_at']

# Simple User Registration serializer
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
