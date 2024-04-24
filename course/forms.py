from django import forms 
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        

        exclude = ['course_total_registered','status','instructor']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',  # Add Bootstrap class
                'placeholder': f'Enter {field.label}'  # Add placeholder
            })