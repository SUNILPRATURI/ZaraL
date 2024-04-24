from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import NotesForm

from .models import Note
# Create your views here.
@login_required
def index(request):
    
    context = {
        'notes': Note.objects.all(),
        'total_notes':Note.objects.all().count(),
        'form':NotesForm(),
    }
    return render(request,'notes/index.html',context)

@login_required
def add_notes(request):
    context = {
        'addNotes':NotesForm()
    }
    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            
            try:
                if request.user.is_authenticated and (request.user.role == 'INSTRUCTOR' or request.user.role == 'ADMIN'):

                    form.save()
                    return redirect('notes') 
                else:
                    return render(request,'notes/base/404.html')
            except :
                return render(request,'notes/base/404.html')

    return render(request,'notes/add.html',context)

@login_required
def view_notes(request,id):
    context = {
        'notes':Note.objects.get(pk=id)
    }
    return render(request,'notes/view_notes.html',context)

@login_required
def view_student_notes(request,id):
    context = {
        'notes':Note.objects.get(pk=id)
    }
    return render(request,'students/view_notes.html',context)

@login_required
def edit_notes(request,id):
    instance = Note.objects.get(pk=id)
    editCourse = NotesForm(instance = instance)
    if request.method == 'POST':
        form = NotesForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('view_notes',id=id)
        else:

            context = {
                'addNotes':form
            }
            return render(request,'notes/add.html',context)
    context = {
        'editNotes':editCourse
    }
    return render(request,'notes/add.html',context)     
    
