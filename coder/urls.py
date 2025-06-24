from django.urls import path, include
from .views import about

appname = 'coder'

urls = [
    path('about/', about, name='about'),
]

coder_patterns = (urls, appname)

urlpatterns = [
    path('', include(coder_patterns)),
]