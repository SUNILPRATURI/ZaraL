from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import  AuthenticationForm, PasswordChangeForm

from django.contrib.auth import update_session_auth_hash

from django.contrib import messages
from django.shortcuts import render, redirect

from django.urls import reverse
from notes.models import Note
from .models import CustomUser

from .forms import CustomUserCreationForm as UserCreationForm,PasswordChangeNoAuthForm,StudentCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect(reverse('redirect-login')+'?registered=true')
        else:
            print(request.POST)
            print(form.errors)  # Print form errors for debugging
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

def register_student(request):
    if request.method == 'POST':
        form = StudentCreationForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect(reverse('redirect-login')+'?registered=true')
        else:
            print(request.POST)
            print(form.errors)  # Print form errors for debugging
    else:
        form = StudentCreationForm()
    return render(request, 'students/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)
                return redirect('index')
             
        else:
            form = AuthenticationForm(request)
            return redirect(reverse('login'))
    else:
        form = AuthenticationForm()
    return render(request, 'auth/login.html', {'form': form})

def redirect_login(request):
    return render(request,'auth/redirect-login.html')

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def change_password_auth(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your password was successfully updated!')
            return redirect('login')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'auth/change_password.html', {'form': form})




def change_password_no_auth(request):
    if request.method == 'POST':
        form = PasswordChangeNoAuthForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            try:
                user = CustomUser.objects.get(username=username)
                user.set_password(password)
                user.save()
                messages.success(request, 'Your password was successfully updated!')
                return redirect(reverse('redirect-login') + '?password_changed=true')   # Redirect to login page after successful password change
            except CustomUser.DoesNotExist:
                form.add_error('username', 'User with this username does not exist.')
    else:
        form = PasswordChangeNoAuthForm()
    return render(request, 'auth/change_password_no_auth.html', {'form': form})


@login_required
def home(request):
    return render(request,'auth/rooms.html')


@login_required
def index(request):
     context = {
        'notes': Note.objects.all(),
        }
     return render(request,'students/index.html',context)