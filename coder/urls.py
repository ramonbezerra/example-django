from django.urls import path, include
from .views import about, index, detail, create, update, delete

appname = 'coder'

urls = [
    path('about/', about, name='about'),
    path('', index, name='index'),
    path('detail/<int:student_id>/', detail, name='detail'),
    path('create/', create, name='create'),
    path('update/<int:student_id>/', update, name='update'),
    path('delete/<int:student_id>/', delete, name='delete'),
]

coder_patterns = (urls, appname)

urlpatterns = [
    path('', include(coder_patterns)),
]