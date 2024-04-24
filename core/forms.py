from django import forms
from .models import Student,CustomUser,Instructor

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete': 'off'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete': 'off'}))
    first_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'})) 
    username = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'})) 
    last_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'}))  
    gender = forms.ChoiceField(choices=(("Male", "Male"), ("Female", "Female"), ("Other", "Other")), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select your gender'}))
    

    class Meta:
        model = CustomUser
        fields = ('username', 'password1', 'password2', 'image', 'gender', 'first_name', 'last_name')
       

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
   
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    


class StudentCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete': 'off'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete': 'off'}))
    first_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'})) 
    username = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'})) 
    last_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'}))  
    gender = forms.ChoiceField(choices=(("Male", "Male"), ("Female", "Female"), ("Other", "Other")), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select your gender'}))
    

    class Meta:
        model = Student
        fields = ('username', 'password1', 'password2', 'image', 'gender', 'first_name', 'last_name')
        widgets = {
            'role': forms.HiddenInput(attrs={'value': 'STUDENT'})
        }

    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
   
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'STUDENT'  # Ensure role is set to STUDENT
        if commit:
            user.save()
        return user


class TeacherCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete': 'off'}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={'class':'form-control','autocomplete': 'off'}))
    first_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'})) 
    username = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'})) 
    last_name = forms.CharField(max_length=30, required=True,widget=forms.TextInput(attrs={'class':'form-control','autocomplete': 'off'}))  
    gender = forms.ChoiceField(choices=(("Male", "Male"), ("Female", "Female"), ("Other", "Other")), widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select your gender'}))
    

    class Meta:
        model = Student
        fields = ('username', 'password1', 'password2', 'image', 'gender', 'first_name', 'last_name')
        widgets = {
            'role': forms.HiddenInput(attrs={'value': 'STUDENT'})
        }

    
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
   
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'INSTRCTOR'  # Ensure role is set to STUDENT
        if commit:
            user.save()
        return user

class PasswordChangeNoAuthForm(forms.Form):
    username = forms.CharField(label='Username', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirm_password = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if not CustomUser.objects.filter(username=username).exists():
            raise forms.ValidationError("User with this username does not exist.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data