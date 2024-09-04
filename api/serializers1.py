from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']  # Adjust fields as needed

class ClientSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    created_by = serializers.PrimaryKeyRelatedField(read_only=True)  # Make created_by read-only

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'updated_at', 'created_by', 'projects']


class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.client_name', read_only=True)
    users = UserSerializer(many=True, read_only=True)  # Use nested serializer for detailed user info
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all(), required=True)  # Ensure client is required

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'client_name', 'users', 'created_at', 'updated_at', 'created_by']
