from django.shortcuts import render
from django.http import HttpResponse
from .models import Student

# Create your views here.
def about(request):
    return HttpResponse("Hello, this is the about page of the coder app.")

def index(request):
    context = {'students': Student.objects.all()}
    return render(request, 'coder/index.html', context)

def detail(request, student_id):
    context = {'student': Student.objects.get(id=student_id)}
    return render(request, 'coder/detail.html', context)
