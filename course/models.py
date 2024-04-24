from django.db import models

from core.models import CustomUser

# Create your models here.
class Course(models.Model):
    
    course_Id = models.CharField(max_length=155, verbose_name='Course ID')
    course_name = models.CharField(max_length=255, verbose_name='Course Name', blank=False, null=False)
    course_description = models.TextField(verbose_name='Course Description', blank=False, null=False)
    course_total_registered = models.PositiveIntegerField(verbose_name='Total Students', default=0)
    status = models.BooleanField(default=True)
    instructor = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='courses', verbose_name='Instructor', null=True)

   
    def __str__(self):
        return self.course_name
    