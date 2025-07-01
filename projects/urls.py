from django.urls import path, include
from .views import ProjectCreateView, ProjectDeleteView, ProjectListView, ProjectDetailView, ProjectUpdateView

appname = 'projects'

urls = [
    path('', ProjectListView.as_view(), name='index'),
    path('detail/<int:pk>/', ProjectDetailView.as_view(), name='detail'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('update/<int:pk>/', ProjectUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', ProjectDeleteView.as_view(), name='delete'),
]

project_patterns = (urls, appname)

urlpatterns = [
    path('', include(project_patterns)),
]
