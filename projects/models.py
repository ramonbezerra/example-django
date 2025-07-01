from django import forms
from django.db import models
import datetime

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date']
    
    name = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Nome do Projeto"
        self.fields['description'].label = "Descrição"
        self.fields['start_date'].label = "Data de Início"
        self.fields['end_date'].label = "Data de Término"

    def clean_name(self):
        data = self.cleaned_data['name']
        if len(data) < 3:
            raise forms.ValidationError("O nome do projeto precisa ter mais de 3 caracteres.")
        return data
    
    def clean_description(self):
        data = self.cleaned_data['description']
        if len(data) < 10:
            raise forms.ValidationError("A descrição precisa ter mais de 10 caracteres.")
        return data

    def clean_start_date(self):
        data = self.cleaned_data.get('start_date')
        if data is not None and self.cleaned_data.get('end_date') is not None:
            if data > self.cleaned_data.get('end_date'):
                raise forms.ValidationError("A data de início não pode ser maior que a data de término.")
        if data > datetime.date.today():
            raise forms.ValidationError("A data de início não pode ser maior que a data atual.")
        return data

    def clean_end_date(self):
        data = self.cleaned_data['end_date']
        start_date = self.cleaned_data.get('start_date')
        if start_date is not None and data < start_date:
            raise forms.ValidationError("A data de término não pode ser menor que a data de início.")
        return data