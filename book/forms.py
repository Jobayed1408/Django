from django import forms 
from book.models import TaskModel

class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskModel
        # fields = "__all__"
        fields = ['taskTitle', 'taskDescription', 'is_completed']
        

        
        
        