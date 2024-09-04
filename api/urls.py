from django.urls import path
from .views import (
    ClientListCreateView, ClientRetrieveUpdateDestroyView,
    ProjectCreateView, ProjectListView, ProjectDeleteView
)

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientRetrieveUpdateDestroyView.as_view(), name='client-detail'),
    path('clients/<int:client_id>/projects/', ProjectListView.as_view(), name='client-projects'), 
    path('projects/', ProjectCreateView.as_view(), name='project-create'),
    path('projects/<int:pk>/', ProjectDeleteView.as_view(), name='project-delete'),
]
