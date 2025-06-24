from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Student, StudentForm

# Create your views here.
def about(request):
    return HttpResponse("Hello, this is the about page of the coder app.")

def index(request):
    context = {'students': Student.objects.all()}
    return render(request, 'coder/index.html', context)

def detail(request, student_id):
    context = {'student': Student.objects.get(id=student_id)}
    return render(request, 'coder/detail.html', context)

def create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if not form.is_valid():
            return render(request, 'coder/create.html', {'form': form})
        else:
            student = Student.objects.create(**form.cleaned_data)
            student.save()
            return redirect('coder:index')
    return render(request, 'coder/create.html', {'form': StudentForm()})