from django.urls import path, include
from .views import about, index, detail, create, update

appname = 'coder'

urls = [
    path('about/', about, name='about'),
    path('', index, name='index'),
    path('detail/<int:student_id>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('update/<int:student_id>/', update, name='update'),
]

coder_patterns = (urls, appname)

urlpatterns = [
    path('', include(coder_patterns)),
]