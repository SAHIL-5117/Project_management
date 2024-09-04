from django.urls import path
from .views import ClientListCreateView, ClientRetrieveUpdateDestroyView, ProjectListCreateDeleteView, ProjectRetrieveUpdateDestroyView, ClientProjectsListView

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-retrieve-update-destroy'),
    path('projects/', ProjectListCreateDeleteView.as_view(), name='project-list-create-delete'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-retrieve-update-destroy'),
    path('clients/<int:client_id>/projects/', ClientProjectsListView.as_view(), name='client-projects-list'),
]
