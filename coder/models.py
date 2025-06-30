from django.db import models
from django import forms

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email']
    
    name = forms.CharField(max_length=100)
    age = forms.IntegerField()
    email = forms.EmailField()

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)