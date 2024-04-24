from django import forms


from .models import Assignment,Submission
class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        exclude =['status']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control',  # Add Bootstrap class
                'placeholder': f'Enter {field.label}'  # Add placeholder
            })