from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required

from .models import Assignment,Submission

from .forms import AssignmentForm

# Create your views here.

@login_required
def index(request):
    
    context = {
        'assignments': Assignment.objects.all(),
        'total_assignments':Assignment.objects.all().count(),
        'form':AssignmentForm(),
    }
    return render(request,'assignments/index.html',context)


@login_required
def add_assignment(request):
    context = {
        'addAssignment':AssignmentForm()
    }
    if request.method == 'POST':
        form = AssignmentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('assignments')
        else:
            context = {
                'addAssignment':form
            }
            return render(request,'assignments/add.html',context)
    return render(request,'assignments/add.html',context)

@login_required
def view_assignment(request,id):
    context = {
        'assignment':Assignment.objects.get(pk=id)
    }
    return render(request,'assignments/view_assign.html',context)


login_required
def edit_assignment(request,id):
    instance = Assignment.objects.get(pk=id)
    editCourse = AssignmentForm(instance = instance)
    if request.method == 'POST':
        form = AssignmentForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('view-assignment',id=id)
        else:
            print(form.errors)
            context = {
                'addAssignment':form
            }
            return render(request,'assignments/add.html',context)
    context = {
        'editAssignment':editCourse
    }
    return render(request,'assignments/add.html',context)     

login_required
def deactivate_assignment(request, id):

    assignments = Assignment.objects.get(pk=id)
  
    if assignments.status == False:
        assignments.status = True
    else:
        assignments.status = False
    assignments.save()

    return redirect('assignments')