from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['user', 'detail', 'type']
        widgets = {
            'type': forms.Select(choices=Task.TASK_TYPES, attrs={'class': 'form-control'}),
        }
