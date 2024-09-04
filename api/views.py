from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from django.shortcuts import get_object_or_404

from .models import Client, Project
from .serializers1 import ClientSerializer, ProjectSerializer

# Clients
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set the `created_by` field to the currently authenticated user
        serializer.save(created_by=self.request.user)

class ClientRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]

# Projects
class ProjectListCreateDeleteView(generics.GenericAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Filter projects by the logged-in user
        return Project.objects.filter(users=self.request.user)

    def get(self, request, *args, **kwargs):
        # Handle GET request
        projects = self.get_queryset()
        serializer = self.serializer_class(projects, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        # Handle POST request
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=self.request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        # Handle DELETE request
        try:
            project_id = request.data.get('id')
            project = get_object_or_404(Project, id=project_id)
            self.check_object_permissions(request, project)
            project.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NotFound:
            return Response({"detail": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NotFound:
            return Response({"detail": "Project not found"}, status=status.HTTP_404_NOT_FOUND)
        
class ClientProjectsListView(generics.ListAPIView):
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        client_id = self.kwargs.get('client_id')
        return Project.objects.filter(client_id=client_id)
