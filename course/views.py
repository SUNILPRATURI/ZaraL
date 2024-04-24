from django.shortcuts import render,redirect

from django.contrib.auth.decorators import login_required
from .forms import CourseForm

from .models import Course
# Create your views here.

@login_required
def index(request):
    
    context = {
        'courses': Course.objects.all(),
        'total_courses':Course.objects.all().count(),
        'form':CourseForm(),
    }
    return render(request,'courses/index.html',context)

@login_required
def add_course(request):
    context = {
        'addCourse':CourseForm()
    }
    if request.method == 'POST':
        print(request.POST['course_name'])
        print(request.user.is_authenticated)
        form = CourseForm(request.POST)
        if form.is_valid():
            
            try:
                if request.user.is_authenticated and (request.user.role == 'INSTRUCTOR' or request.user.role == 'ADMIN'):
                    
                    cleaned_data = form.cleaned_data
                    course_name = cleaned_data['course_name']
                    course_description = cleaned_data['course_description']
                    course = Course(course_name=course_name, course_description=course_description, instructor=request.user)
                    print(request.user.role)
                    course.save()
                    
                    
                    return redirect('courses') 
                else:
                    return render(request,'courses/base/404.html')
            except :
                
                return render(request,'courses/base/404.html')
        

           
    return render(request,'courses/add.html',context)

@login_required
def view_course(request,id):
    context = {
        'course':Course.objects.get(pk=id)
    }
    return render(request,'courses/view_course.html',context)
@login_required
def edit_course(request,id):
    instance = Course.objects.get(pk=id)
    editCourse = CourseForm(instance = instance)
    if request.method == 'POST':
        form = CourseForm(request.POST,instance=instance)
        if form.is_valid():
            form.save()
            return redirect('view_course',id=id)
        else:
            print(form.errors)
            context = {
                'addCourse':form
            }
            return render(request,'courses/edit.html',context)
    context = {
        'editCourse':editCourse
    }
    return render(request,'courses/edit.html',context) 
    
@login_required  
def deactivate_course(request, id):

    course = Course.objects.get(pk=id)
  
    if course.status == False:
        course.status = True
    else:
        course.status = False
    course.save()

    return redirect('courses')
