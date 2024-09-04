from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name']

class ClientSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    created_by = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['id', 'client_name', 'created_at', 'updated_at', 'created_by', 'projects']

    def get_created_by(self, obj):
        return obj.created_by.username  


class ProjectSerializer(serializers.ModelSerializer):
    client_name = serializers.CharField(source='client.client_name', read_only=True)
    created_by = serializers.SlugRelatedField(
        slug_field='username', 
        queryset=User.objects.all(), 
        required=False  # Make it optional so it can be set manually or auto-filled
    )

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'client', 'client_name', 'created_by', 'created_at']

