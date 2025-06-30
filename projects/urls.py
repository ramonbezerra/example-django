from django.urls import path, include
from .views import ProjectListView, ProjectDetailView

appname = 'projects'

urls = [
    path('', ProjectListView.as_view(), name='index'),
    path('detail/<int:pk>/', ProjectDetailView.as_view(), name='detail'),
]

project_patterns = (urls, appname)

urlpatterns = [
    path('', include(project_patterns)),
]
