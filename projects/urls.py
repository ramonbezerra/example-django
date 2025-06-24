from django.urls import path, include
from .views import index, detail

appname = 'projects'

urls = [
    path('', index, name='index'),
    path('detail/<int:project_id>/', detail, name='detail'),
]

project_patterns = (urls, appname)

urlpatterns = [
    path('', include(project_patterns)),
]
